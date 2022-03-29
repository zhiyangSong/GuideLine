# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dag_graph.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import graph_pb2 as graph__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dag_graph.proto',
  package='haomo.hidelivery.guard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0f\x64\x61g_graph.proto\x12\x16haomo.hidelivery.guard\x1a\x0cheader.proto\x1a\x0bgraph.proto\"_\n\nDagGraphPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12-\n\tdag_graph\x18\x02 \x01(\x0b\x32\x1a.base.graph.graphviz.Graphb\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,graph__pb2.DESCRIPTOR,])




_DAGGRAPHPB = _descriptor.Descriptor(
  name='DagGraphPb',
  full_name='haomo.hidelivery.guard.DagGraphPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.guard.DagGraphPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dag_graph', full_name='haomo.hidelivery.guard.DagGraphPb.dag_graph', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=165,
)

_DAGGRAPHPB.fields_by_name['header'].message_type = header__pb2._HEADER
_DAGGRAPHPB.fields_by_name['dag_graph'].message_type = graph__pb2._GRAPH
DESCRIPTOR.message_types_by_name['DagGraphPb'] = _DAGGRAPHPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DagGraphPb = _reflection.GeneratedProtocolMessageType('DagGraphPb', (_message.Message,), {
  'DESCRIPTOR' : _DAGGRAPHPB,
  '__module__' : 'dag_graph_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.guard.DagGraphPb)
  })
_sym_db.RegisterMessage(DagGraphPb)


# @@protoc_insertion_point(module_scope)
