# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ota_state.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ota_state.proto',
  package='haomo.hidelivery.ota',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0fota_state.proto\x12\x14haomo.hidelivery.ota\x1a\x0cheader.proto\"|\n\x0eOtaStateOutput\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x31\n\tota_state\x18\x02 \x01(\x0e\x32\x1e.haomo.hidelivery.ota.OtaState\x12\x13\n\x0bsys_time_us\x18\x03 \x01(\x04*\x7f\n\x08OtaState\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\x13\n\x0fLINK_REQUESTING\x10\x02\x12\x0f\n\x0b\x44OWNLOADING\x10\x03\x12\x0b\n\x07PARSING\x10\x04\x12\x0f\n\x0b\x46SM_WAITING\x10\x05\x12\x0c\n\x08UPDATING\x10\x06\x12\n\n\x06\x46INISH\x10\x07\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_OTASTATE = _descriptor.EnumDescriptor(
  name='OtaState',
  full_name='haomo.hidelivery.ota.OtaState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINK_REQUESTING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOADING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARSING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FSM_WAITING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISH', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=181,
  serialized_end=308,
)
_sym_db.RegisterEnumDescriptor(_OTASTATE)

OtaState = enum_type_wrapper.EnumTypeWrapper(_OTASTATE)
DEFAULT = 0
IDLE = 1
LINK_REQUESTING = 2
DOWNLOADING = 3
PARSING = 4
FSM_WAITING = 5
UPDATING = 6
FINISH = 7



_OTASTATEOUTPUT = _descriptor.Descriptor(
  name='OtaStateOutput',
  full_name='haomo.hidelivery.ota.OtaStateOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.ota.OtaStateOutput.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ota_state', full_name='haomo.hidelivery.ota.OtaStateOutput.ota_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.ota.OtaStateOutput.sys_time_us', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=55,
  serialized_end=179,
)

_OTASTATEOUTPUT.fields_by_name['header'].message_type = header__pb2._HEADER
_OTASTATEOUTPUT.fields_by_name['ota_state'].enum_type = _OTASTATE
DESCRIPTOR.message_types_by_name['OtaStateOutput'] = _OTASTATEOUTPUT
DESCRIPTOR.enum_types_by_name['OtaState'] = _OTASTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OtaStateOutput = _reflection.GeneratedProtocolMessageType('OtaStateOutput', (_message.Message,), {
  'DESCRIPTOR' : _OTASTATEOUTPUT,
  '__module__' : 'ota_state_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.ota.OtaStateOutput)
  })
_sym_db.RegisterMessage(OtaStateOutput)


# @@protoc_insertion_point(module_scope)
