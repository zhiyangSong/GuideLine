# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cloud_control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cloud_control.proto',
  package='haomo.hidelivery',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13\x63loud_control.proto\x12\x10haomo.hidelivery\x1a\x0cheader.proto\"\xc6\x01\n\x10\x43loudControlData\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0b\x63loud_estop\x18\x02 \x01(\x08\x12\x14\n\x0c\x63loud_remote\x18\x03 \x01(\x08\x12$\n\x1c\x63loud_double_flash_light_cmd\x18\x04 \x01(\r\x12\x11\n\tcmd_angle\x18\x05 \x01(\x01\x12\x11\n\tcmd_speed\x18\x06 \x01(\x01\x12\x17\n\x0f\x63md_brake_pedal\x18\x07 \x01(\r\"E\n\x0cWebEstopData\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x11\n\tweb_estop\x18\x02 \x01(\x08\"h\n\x0c\x43\x61meraPushPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x11\n\tcamera_id\x18\x02 \x01(\t\x12\x0f\n\x07is_push\x18\x03 \x01(\x08\x12\x10\n\x08rtmp_url\x18\x04 \x01(\tb\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])




_CLOUDCONTROLDATA = _descriptor.Descriptor(
  name='CloudControlData',
  full_name='haomo.hidelivery.CloudControlData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CloudControlData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_estop', full_name='haomo.hidelivery.CloudControlData.cloud_estop', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_remote', full_name='haomo.hidelivery.CloudControlData.cloud_remote', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_double_flash_light_cmd', full_name='haomo.hidelivery.CloudControlData.cloud_double_flash_light_cmd', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd_angle', full_name='haomo.hidelivery.CloudControlData.cmd_angle', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd_speed', full_name='haomo.hidelivery.CloudControlData.cmd_speed', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd_brake_pedal', full_name='haomo.hidelivery.CloudControlData.cmd_brake_pedal', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=56,
  serialized_end=254,
)


_WEBESTOPDATA = _descriptor.Descriptor(
  name='WebEstopData',
  full_name='haomo.hidelivery.WebEstopData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.WebEstopData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='web_estop', full_name='haomo.hidelivery.WebEstopData.web_estop', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=256,
  serialized_end=325,
)


_CAMERAPUSHPB = _descriptor.Descriptor(
  name='CameraPushPb',
  full_name='haomo.hidelivery.CameraPushPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CameraPushPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='haomo.hidelivery.CameraPushPb.camera_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_push', full_name='haomo.hidelivery.CameraPushPb.is_push', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtmp_url', full_name='haomo.hidelivery.CameraPushPb.rtmp_url', index=3,
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
  serialized_start=327,
  serialized_end=431,
)

_CLOUDCONTROLDATA.fields_by_name['header'].message_type = header__pb2._HEADER
_WEBESTOPDATA.fields_by_name['header'].message_type = header__pb2._HEADER
_CAMERAPUSHPB.fields_by_name['header'].message_type = header__pb2._HEADER
DESCRIPTOR.message_types_by_name['CloudControlData'] = _CLOUDCONTROLDATA
DESCRIPTOR.message_types_by_name['WebEstopData'] = _WEBESTOPDATA
DESCRIPTOR.message_types_by_name['CameraPushPb'] = _CAMERAPUSHPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CloudControlData = _reflection.GeneratedProtocolMessageType('CloudControlData', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDCONTROLDATA,
  '__module__' : 'cloud_control_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CloudControlData)
  })
_sym_db.RegisterMessage(CloudControlData)

WebEstopData = _reflection.GeneratedProtocolMessageType('WebEstopData', (_message.Message,), {
  'DESCRIPTOR' : _WEBESTOPDATA,
  '__module__' : 'cloud_control_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.WebEstopData)
  })
_sym_db.RegisterMessage(WebEstopData)

CameraPushPb = _reflection.GeneratedProtocolMessageType('CameraPushPb', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAPUSHPB,
  '__module__' : 'cloud_control_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CameraPushPb)
  })
_sym_db.RegisterMessage(CameraPushPb)


# @@protoc_insertion_point(module_scope)