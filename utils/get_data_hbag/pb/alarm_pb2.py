# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alarm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alarm.proto',
  package='haomo.hidelivery.guard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x61larm.proto\x12\x16haomo.hidelivery.guard\x1a\x0cheader.proto\"x\n\x07\x41larmPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x0e\n\x06module\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\x04\x12\x0f\n\x07timeout\x18\x05 \x01(\x04\x12\x0b\n\x03msg\x18\x06 \x01(\tb\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])




_ALARMPB = _descriptor.Descriptor(
  name='AlarmPb',
  full_name='haomo.hidelivery.guard.AlarmPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.guard.AlarmPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='haomo.hidelivery.guard.AlarmPb.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='haomo.hidelivery.guard.AlarmPb.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='haomo.hidelivery.guard.AlarmPb.time', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='haomo.hidelivery.guard.AlarmPb.timeout', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='haomo.hidelivery.guard.AlarmPb.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=53,
  serialized_end=173,
)

_ALARMPB.fields_by_name['header'].message_type = header__pb2._HEADER
DESCRIPTOR.message_types_by_name['AlarmPb'] = _ALARMPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlarmPb = _reflection.GeneratedProtocolMessageType('AlarmPb', (_message.Message,), {
  'DESCRIPTOR' : _ALARMPB,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.guard.AlarmPb)
  })
_sym_db.RegisterMessage(AlarmPb)


# @@protoc_insertion_point(module_scope)
