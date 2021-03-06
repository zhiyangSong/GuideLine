# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ota_result.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import ota_update_pb2 as ota__update__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ota_result.proto',
  package='haomo.hidelivery.ota',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10ota_result.proto\x12\x14haomo.hidelivery.ota\x1a\x0cheader.proto\x1a\x10ota_update.proto\"\xb6\x01\n\x0bOtaResultPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x36\n\x0bupdate_info\x18\x02 \x01(\x0b\x32!.haomo.hidelivery.ota.OtaUpdatePb\x12\x39\n\rupdate_result\x18\x03 \x01(\x0e\x32\".haomo.hidelivery.ota.UpdateResult\x12\x10\n\x08\x65rr_info\x18\x04 \x01(\t*%\n\x0cUpdateResult\x12\x08\n\x04\x46\x41IL\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,ota__update__pb2.DESCRIPTOR,])

_UPDATERESULT = _descriptor.EnumDescriptor(
  name='UpdateResult',
  full_name='haomo.hidelivery.ota.UpdateResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=259,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_UPDATERESULT)

UpdateResult = enum_type_wrapper.EnumTypeWrapper(_UPDATERESULT)
FAIL = 0
SUCCESS = 1



_OTARESULTPB = _descriptor.Descriptor(
  name='OtaResultPb',
  full_name='haomo.hidelivery.ota.OtaResultPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.ota.OtaResultPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_info', full_name='haomo.hidelivery.ota.OtaResultPb.update_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_result', full_name='haomo.hidelivery.ota.OtaResultPb.update_result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_info', full_name='haomo.hidelivery.ota.OtaResultPb.err_info', index=3,
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
  serialized_start=75,
  serialized_end=257,
)

_OTARESULTPB.fields_by_name['header'].message_type = header__pb2._HEADER
_OTARESULTPB.fields_by_name['update_info'].message_type = ota__update__pb2._OTAUPDATEPB
_OTARESULTPB.fields_by_name['update_result'].enum_type = _UPDATERESULT
DESCRIPTOR.message_types_by_name['OtaResultPb'] = _OTARESULTPB
DESCRIPTOR.enum_types_by_name['UpdateResult'] = _UPDATERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OtaResultPb = _reflection.GeneratedProtocolMessageType('OtaResultPb', (_message.Message,), {
  'DESCRIPTOR' : _OTARESULTPB,
  '__module__' : 'ota_result_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.ota.OtaResultPb)
  })
_sym_db.RegisterMessage(OtaResultPb)


# @@protoc_insertion_point(module_scope)
