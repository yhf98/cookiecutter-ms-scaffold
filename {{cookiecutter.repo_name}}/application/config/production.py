"""
BaseAuth 配置
"""
AUTH_USER="admin"
AUTH_PASSWORD="password"

"""
Mysql 数据库配置项
连接引擎官方文档：https://www.osgeo.cn/sqlalchemy/core/engines.html
数据库链接配置说明：mysql+asyncmy://数据库用户名:数据库密码@数据库地址:数据库端口/数据库名称
"""
SQLALCHEMY_DATABASE_URL = "mysql+asyncmy://root:123456@127.0.0.1:3306/test"
SQLALCHEMY_DATABASE_URL_SECONDARY = "mysql+asyncmy://root:123456@127.0.0.1:3306/test-test"

"""
Redis 数据库配置
格式："redis://:密码@地址:端口/数据库名称"
"""
REDIS_DB_ENABLE = False
REDIS_DB_URL = "redis://:123456@127.0.0.1:6379/1"
WARNING_KEY="warning"
WARNING_VALUE=20
"""
MongoDB 数据库配置
格式：mongodb://用户名:密码@地址:端口/?authSource=数据库名称
"""
MONGO_DB_ENABLE = False
MONGO_DB_NAME = "ms-api"
MONGO_DB_URL = f"mongodb://ms-api:123456@127.0.0.1:27017/?authSource={MONGO_DB_NAME}"


"""
阿里云对象存储OSS配置
阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
 *  [accessKeyId] {String}：通过阿里云控制台创建的AccessKey。
 *  [accessKeySecret] {String}：通过阿里云控制台创建的AccessSecret。
 *  [bucket] {String}：通过控制台或PutBucket创建的bucket。
 *  [endpoint] {String}：bucket所在的区域， 默认oss-cn-hangzhou。
"""
ALIYUN_OSS = {
    "accessKeyId": "",
    "accessKeySecret": "",
    "endpoint": "",
    "bucket": "",
    "baseUrl": ""
}

"""
获取IP地址归属地
文档：https://user.ip138.com/ip/doc
"""
IP_PARSE_ENABLE = False
IP_PARSE_TOKEN = "74ddc2a51ea0a0fe96955e8adc1ef634"

"""
RabbitMQ
"""
RABBIT_ENABLE = False
RABBIT_HOST="127.0.0.1"
RABBIT_PORT=5672
RABBIT_USER="guest"
RABBIT_PASSWORD="123456"
EXCHANGE="api_usage"
API_UASGE_QUEUE="api_usage_queue"
API_UASGE_ROUTE="api_usage_key"