# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ota_update.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ota_update.proto',
  package='haomo.hidelivery.ota',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10ota_update.proto\x12\x14haomo.hidelivery.ota\x1a\x0cheader.proto\"\x83\x01\n\x0bOtaUpdatePb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .haomo.hidelivery.ota.UpdateType\x12\x0e\n\x06module\x18\x03 \x01(\t\x12\x10\n\x08\x66ile_md5\x18\x04 \x01(\t*,\n\nUpdateType\x12\n\n\x06\x43ONFIG\x10\x00\x12\x08\n\x04SOTA\x10\x01\x12\x08\n\x04\x46OTA\x10\x02\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='haomo.hidelivery.ota.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOTA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOTA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=190,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_UPDATETYPE)

UpdateType = enum_type_wrapper.EnumTypeWrapper(_UPDATETYPE)
CONFIG = 0
SOTA = 1
FOTA = 2



_OTAUPDATEPB = _descriptor.Descriptor(
  name='OtaUpdatePb',
  full_name='haomo.hidelivery.ota.OtaUpdatePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.ota.OtaUpdatePb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='haomo.hidelivery.ota.OtaUpdatePb.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='haomo.hidelivery.ota.OtaUpdatePb.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_md5', full_name='haomo.hidelivery.ota.OtaUpdatePb.file_md5', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=57,
  serialized_end=188,
)

_OTAUPDATEPB.fields_by_name['header'].message_type = header__pb2._HEADER
_OTAUPDATEPB.fields_by_name['type'].enum_type = _UPDATETYPE
DESCRIPTOR.message_types_by_name['OtaUpdatePb'] = _OTAUPDATEPB
DESCRIPTOR.enum_types_by_name['UpdateType'] = _UPDATETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OtaUpdatePb = _reflection.GeneratedProtocolMessageType('OtaUpdatePb', (_message.Message,), {
  'DESCRIPTOR' : _OTAUPDATEPB,
  '__module__' : 'ota_update_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.ota.OtaUpdatePb)
  })
_sym_db.RegisterMessage(OtaUpdatePb)


# @@protoc_insertion_point(module_scope)
