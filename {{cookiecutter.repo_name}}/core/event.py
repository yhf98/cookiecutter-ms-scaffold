import asyncio
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from application.settings import REDIS_DB_URL, MONGO_DB_URL, MONGO_DB_NAME, EVENTS, TRACER_EVENTS, CONSUMER_EVENTS, RABBIT_HOST,RABBIT_USER,RABBIT_PASSWORD, RABBIT_PORT
from utils.cache import Cache
from redis import asyncio as aioredis
from redis.exceptions import AuthenticationError, TimeoutError, RedisError
from contextlib import asynccontextmanager
from utils.tools import import_modules_async
from sqlalchemy.exc import ProgrammingError
from core.logger import logger
from core.rabbit_manage import RabbitMQ
from core.consumers import start_consumer_new_thread, start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await import_modules_async(EVENTS, "全局事件", app=app, status=True)

    yield

    await import_modules_async(EVENTS, "全局事件", app=app, status=False)
    
@asynccontextmanager
async def tracer_lifespan(app: FastAPI):
    print("Tracer 全局事件")
    await import_modules_async(TRACER_EVENTS, "全局事件", app=app, status=True)

    yield

    await import_modules_async(TRACER_EVENTS, "全局事件", app=app, status=False)
    
@asynccontextmanager
async def consumer_lifespan(app: FastAPI):
    print("Consumer 全局事件")
    await import_modules_async(CONSUMER_EVENTS, "全局事件", app=app, status=True)

    yield

    await import_modules_async(CONSUMER_EVENTS, "全局事件", app=app, status=False)
    


async def connect_redis(app: FastAPI, status: bool):
    """
    把 redis 挂载到 app 对象上面

    博客：https://blog.csdn.net/wgPython/article/details/107668521
    博客：https://www.cnblogs.com/emunshe/p/15761597.html
    官网：https://aioredis.readthedocs.io/en/latest/getting-started/
    Github: https://github.com/aio-libs/aioredis-py

    aioredis.from_url(url, *, encoding=None, parser=None, decode_responses=False, db=None, password=None, ssl=None,
    connection_cls=None, loop=None, **kwargs) 方法是 aioredis 库中用于从 Redis 连接 URL 创建 Redis 连接对象的方法。

    以下是该方法的参数说明：
    url：Redis 连接 URL。例如 redis://localhost:6379/0。
    encoding：可选参数，Redis 编码格式。默认为 utf-8。
    parser：可选参数，Redis 数据解析器。默认为 None，表示使用默认解析器。
    decode_responses：可选参数，是否将 Redis 响应解码为 Python 字符串。默认为 False。
    db：可选参数，Redis 数据库编号。默认为 None。
    password：可选参数，Redis 认证密码。默认为 None，表示无需认证。
    ssl：可选参数，是否使用 SSL/TLS 加密连接。默认为 None。
    connection_cls：可选参数，Redis 连接类。默认为 None，表示使用默认连接类。
    loop：可选参数，用于创建连接对象的事件循环。默认为 None，表示使用默认事件循环。
    **kwargs：可选参数，其他连接参数，用于传递给 Redis 连接类的构造函数。

    aioredis.from_url() 方法的主要作用是将 Redis 连接 URL 转换为 Redis 连接对象。
    除了 URL 参数外，其他参数用于指定 Redis 连接的各种选项，例如 Redis 数据库编号、密码、SSL/TLS 加密等等。可以根据需要选择使用这些选项。

    health_check_interval 是 aioredis.from_url() 方法中的一个可选参数，用于设置 Redis 连接的健康检查间隔时间。
    健康检查是指在 Redis 连接池中使用的连接对象会定期向 Redis 服务器发送 PING 命令来检查连接是否仍然有效。
    该参数的默认值是 0，表示不进行健康检查。如果需要启用健康检查，则可以将该参数设置为一个正整数，表示检查间隔的秒数。
    例如，如果需要每隔 5 秒对 Redis 连接进行一次健康检查，则可以将 health_check_interval 设置为 5
    :param app:
    :param status:
    :return:
    """
    if status:
        # rd = aioredis.from_url(REDIS_DB_URL, decode_responses=True, health_check_interval=1)
        rd = aioredis.from_url(REDIS_DB_URL, decode_responses=True, health_check_interval=5, max_connections=1000)
        app.state.redis = rd
        try:
            response = await rd.ping()
            if response:
                print("Redis 连接成功")
            else:
                print("Redis 连接失败")
        except AuthenticationError as e:
            raise AuthenticationError(f"Redis 连接认证失败，用户名或密码错误: {e}")
        except TimeoutError as e:
            raise TimeoutError(f"Redis 连接超时，地址或者端口错误: {e}")
        except RedisError as e:
            raise RedisError(f"Redis 连接失败: {e}")
        try:
            await Cache(app.state.redis).cache_tab_names()
        except ProgrammingError as e:
            logger.error(f"sqlalchemy.exc.ProgrammingError: {e}")
            print(f"sqlalchemy.exc.ProgrammingError: {e}")
    else:
        print("Redis 连接关闭")
        await app.state.redis.close()


async def connect_mongo(app: FastAPI, status: bool):
    """
    把 mongo 挂载到 app 对象上面

    博客：https://www.cnblogs.com/aduner/p/13532504.html
    mongodb 官网：https://www.mongodb.com/docs/drivers/motor/
    motor 文档：https://motor.readthedocs.io/en/stable/
    :param app:
    :param status:
    :return:
    """
    if status:
        client: AsyncIOMotorClient = AsyncIOMotorClient(
            MONGO_DB_URL,
            maxPoolSize=10,
            minPoolSize=10,
            serverSelectionTimeoutMS=5000
        )
        app.state.mongo_client = client
        app.state.mongo = client[MONGO_DB_NAME]
        # 尝试连接并捕获可能的超时异常
        try:
            # 触发一次服务器通信来确认连接
            data = await client.server_info()
            print("MongoDB 连接成功", data)
        except Exception as e:
            raise ValueError(f"MongoDB 连接失败: {e}")
    else:
        print("MongoDB 连接关闭")
        app.state.mongo_client.close()

async def connect_rabbitmq(app: FastAPI, status: bool):
    if status:
        rabbitmq = RabbitMQ(username=RABBIT_USER, password=RABBIT_PASSWORD, host=RABBIT_HOST, port=RABBIT_PORT)
        app.state.rabbitmq = rabbitmq
        print("RabbitMQ 连接成功")
    # else:
    #     # print("RabbitMQ 连接关闭")
    #     # app.state.rabbitmq.close_connection()
        
async def setup_rabbitmq_consumer(app: FastAPI, status: bool):
    if status:
        start_consumer_new_thread(asyncio.get_event_loop())
    else:
        print("RabbitMQ 消费者已关闭")

