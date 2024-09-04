import time
import grpc
from loguru import logger
from concurrent import futures
from apps.portal.home.services.rpc import helloworld_pb2 as pb2
from apps.portal.home.services.rpc import helloworld_pb2_grpc as pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(pb2.HelloRequest(name='you'))
        print("接收到: " + response.message)
        response = stub.SayHelloAgain(pb2.HelloRequest(name='you'))
        print("接收到: " + response.message)