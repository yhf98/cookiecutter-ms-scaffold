import time
import grpc
from loguru import logger
from concurrent import futures

from apps.portal.home.services.rpc import helloworld_pb2 as pb2
from apps.portal.home.services.rpc import helloworld_pb2_grpc as pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Server(pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return pb2.HelloReply(message=f"Hello, {request.name}!")

    def SayHelloAgain(self, request, context):
        return pb2.HelloReply(message=f"Hello again, {request.name}!")
    

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(Server(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)