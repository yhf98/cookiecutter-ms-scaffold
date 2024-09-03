from loguru import logger

from services.rpc import ms_scaffold_pb2 as pb2
from services.rpc import ms_scaffold_pb2_grpc as pb2_grpc


class Service(pb2_grpc.MsScaffoldServiceServicer):
    pass