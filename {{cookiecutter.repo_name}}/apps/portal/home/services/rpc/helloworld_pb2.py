# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2b\n\x07Greeter\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12-\n\rSayHelloAgain\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=50
  _HELLOREQUEST._serialized_end=78
  _HELLOREPLY._serialized_start=80
  _HELLOREPLY._serialized_end=109
  _GREETER._serialized_start=111
  _GREETER._serialized_end=209
# @@protoc_insertion_point(module_scope)