# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_cmd.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_cmd.proto',
  package='haomo.hidelivery.guard.supervisor',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rhmi_cmd.proto\x12!haomo.hidelivery.guard.supervisor\x1a\x0cheader.proto\"i\n\x06HmiCmd\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.haomo.hidelivery.guard.supervisor.HmiCmdType*>\n\nHmiCmdType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04PING\x10\x01\x12\r\n\tSHUT_DOWN\x10\x02\x12\n\n\x06REBOOT\x10\x03\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_HMICMDTYPE = _descriptor.EnumDescriptor(
  name='HmiCmdType',
  full_name='haomo.hidelivery.guard.supervisor.HmiCmdType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUT_DOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REBOOT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=173,
  serialized_end=235,
)
_sym_db.RegisterEnumDescriptor(_HMICMDTYPE)

HmiCmdType = enum_type_wrapper.EnumTypeWrapper(_HMICMDTYPE)
DEFAULT = 0
PING = 1
SHUT_DOWN = 2
REBOOT = 3



_HMICMD = _descriptor.Descriptor(
  name='HmiCmd',
  full_name='haomo.hidelivery.guard.supervisor.HmiCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.guard.supervisor.HmiCmd.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='haomo.hidelivery.guard.supervisor.HmiCmd.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=66,
  serialized_end=171,
)

_HMICMD.fields_by_name['header'].message_type = header__pb2._HEADER
_HMICMD.fields_by_name['type'].enum_type = _HMICMDTYPE
DESCRIPTOR.message_types_by_name['HmiCmd'] = _HMICMD
DESCRIPTOR.enum_types_by_name['HmiCmdType'] = _HMICMDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HmiCmd = _reflection.GeneratedProtocolMessageType('HmiCmd', (_message.Message,), {
  'DESCRIPTOR' : _HMICMD,
  '__module__' : 'hmi_cmd_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.guard.supervisor.HmiCmd)
  })
_sym_db.RegisterMessage(HmiCmd)


# @@protoc_insertion_point(module_scope)
