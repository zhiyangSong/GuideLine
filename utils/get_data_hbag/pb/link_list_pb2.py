# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: link_list.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='link_list.proto',
  package='haomo.hidelivery.routing',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0flink_list.proto\x12\x18haomo.hidelivery.routing\")\n\x08LinkList\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07lane_id\x18\x02 \x03(\tb\x06proto3'
)




_LINKLIST = _descriptor.Descriptor(
  name='LinkList',
  full_name='haomo.hidelivery.routing.LinkList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='haomo.hidelivery.routing.LinkList.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='haomo.hidelivery.routing.LinkList.lane_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=45,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['LinkList'] = _LINKLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkList = _reflection.GeneratedProtocolMessageType('LinkList', (_message.Message,), {
  'DESCRIPTOR' : _LINKLIST,
  '__module__' : 'link_list_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.routing.LinkList)
  })
_sym_db.RegisterMessage(LinkList)


# @@protoc_insertion_point(module_scope)
