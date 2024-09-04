import pika
import json
import time
from threading import Lock
from application import settings
from application.settings import RABBIT_ENABLE
from core.exception import CustomException
from fastapi import Request
from application.settings import RABBIT_USER, RABBIT_PASSWORD, RABBIT_HOST, RABBIT_PORT

class RabbitMQ:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, username: str = RABBIT_USER, password: str = RABBIT_PASSWORD, host: str = RABBIT_HOST, port: int = RABBIT_PORT):
        credentials = pika.PlainCredentials(username, password)
        parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=settings.EXCHANGE, exchange_type='direct', durable=True)
        self.channel.queue_declare(queue=settings.API_UASGE_QUEUE, durable=True)
        self.channel.queue_bind(exchange=settings.EXCHANGE, queue=settings.API_UASGE_QUEUE, routing_key=settings.API_UASGE_ROUTE)

    def consume_messages(self, callback, loop=None):
        try:
            self.channel.basic_consume(queue=settings.API_UASGE_QUEUE, on_message_callback=callback, auto_ack=False)
            print('消息等待中··· 按下 CTRL+C 终止运行')
            self.channel.start_consuming()
        except pika.exceptions.StreamLostError:
            print("等待重试")
            time.sleep(5) 
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=settings.EXCHANGE, exchange_type='direct', durable=True)
            self.channel.queue_declare(queue=settings.API_UASGE_QUEUE, durable=True)
            self.channel.queue_bind(exchange=settings.EXCHANGE, queue=settings.API_UASGE_QUEUE, routing_key=settings.API_UASGE_ROUTE)
            
            # self.channel.basic_consume(queue=settings.API_UASGE_QUEUE, on_message_callback=callback, auto_ack=False)
            # print('消息等待中··· 按下 CTRL+C 终止运行')
            # self.channel.start_consuming()
        except Exception as e:
            print(f"Unhandled exception: {e}")

    def publish_message(self, message: dict):
        self.channel.basic_publish(
            exchange=settings.EXCHANGE,
            routing_key=settings.API_UASGE_ROUTE,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # 使消息持久化
            )
        )

    # def consume_messages(self, callback):
    #     self.channel.basic_qos(prefetch_count=1)
    #     self.channel.basic_consume(queue=settings.API_UASGE_QUEUE, on_message_callback=callback)
    #     self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()


def rabbit_getter(request: Request):
    """
    获取 RabbitMQ 对象

    全局挂载，使用一个MQ对象
    """
    if not RABBIT_ENABLE:
        raise CustomException("请先配置RabbitMQ链接并启用！", desc="请启用 application/settings.py: RABBIT_ENABLE")
    return request.app.state.rabbitmq