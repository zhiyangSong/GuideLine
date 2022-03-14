# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera_data.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='camera_data.proto',
  package='haomo.hidelivery',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11\x63\x61mera_data.proto\x12\x10haomo.hidelivery\x1a\x0cheader.proto\"\x84\x02\n\x0c\x43\x61meraDataPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x05 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x31\n\x0b\x63olor_space\x18\x07 \x01(\x0e\x32\x1c.haomo.hidelivery.ColorSpace\x12\x35\n\rcompress_type\x18\x08 \x01(\x0e\x32\x1e.haomo.hidelivery.CompressType\x12\x13\n\x0bvideo_stamp\x18\t \x03(\x04\"\x8c\x02\n\x14\x43\x61meraCompressDataPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x05 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x31\n\x0b\x63olor_space\x18\x07 \x01(\x0e\x32\x1c.haomo.hidelivery.ColorSpace\x12\x35\n\rcompress_type\x18\x08 \x01(\x0e\x32\x1e.haomo.hidelivery.CompressType\x12\x13\n\x0bvideo_stamp\x18\t \x03(\x04\"Z\n\x0f\x43\x61meraSigDataPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12\x0e\n\x06status\x18\x03 \x01(\x08\"6\n\x10\x43\x61meraNullDataPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header*7\n\nColorSpace\x12\x0b\n\x07IMG_BGR\x10\x00\x12\x0c\n\x08IMG_YUYV\x10\x01\x12\x0e\n\nIMG_YUV422\x10\x02*_\n\x0c\x43ompressType\x12\x0b\n\x07IMG_RAW\x10\x00\x12\x0c\n\x08IMG_JPEG\x10\x01\x12\x0b\n\x07VID_VP8\x10\x32\x12\x0b\n\x07VID_VP9\x10\x33\x12\x0c\n\x08VID_H264\x10\x34\x12\x0c\n\x08VID_H265\x10\x35\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_COLORSPACE = _descriptor.EnumDescriptor(
  name='ColorSpace',
  full_name='haomo.hidelivery.ColorSpace',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMG_BGR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMG_YUYV', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMG_YUV422', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=735,
  serialized_end=790,
)
_sym_db.RegisterEnumDescriptor(_COLORSPACE)

ColorSpace = enum_type_wrapper.EnumTypeWrapper(_COLORSPACE)
_COMPRESSTYPE = _descriptor.EnumDescriptor(
  name='CompressType',
  full_name='haomo.hidelivery.CompressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMG_RAW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMG_JPEG', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VID_VP8', index=2, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VID_VP9', index=3, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VID_H264', index=4, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VID_H265', index=5, number=53,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=792,
  serialized_end=887,
)
_sym_db.RegisterEnumDescriptor(_COMPRESSTYPE)

CompressType = enum_type_wrapper.EnumTypeWrapper(_COMPRESSTYPE)
IMG_BGR = 0
IMG_YUYV = 1
IMG_YUV422 = 2
IMG_RAW = 0
IMG_JPEG = 1
VID_VP8 = 50
VID_VP9 = 51
VID_H264 = 52
VID_H265 = 53



_CAMERADATAPB = _descriptor.Descriptor(
  name='CameraDataPb',
  full_name='haomo.hidelivery.CameraDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CameraDataPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.CameraDataPb.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='haomo.hidelivery.CameraDataPb.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='haomo.hidelivery.CameraDataPb.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='haomo.hidelivery.CameraDataPb.channel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='haomo.hidelivery.CameraDataPb.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_space', full_name='haomo.hidelivery.CameraDataPb.color_space', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compress_type', full_name='haomo.hidelivery.CameraDataPb.compress_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_stamp', full_name='haomo.hidelivery.CameraDataPb.video_stamp', index=8,
      number=9, type=4, cpp_type=4, label=3,
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
  serialized_start=54,
  serialized_end=314,
)


_CAMERACOMPRESSDATAPB = _descriptor.Descriptor(
  name='CameraCompressDataPb',
  full_name='haomo.hidelivery.CameraCompressDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CameraCompressDataPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.CameraCompressDataPb.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='haomo.hidelivery.CameraCompressDataPb.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='haomo.hidelivery.CameraCompressDataPb.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='haomo.hidelivery.CameraCompressDataPb.channel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='haomo.hidelivery.CameraCompressDataPb.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_space', full_name='haomo.hidelivery.CameraCompressDataPb.color_space', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compress_type', full_name='haomo.hidelivery.CameraCompressDataPb.compress_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_stamp', full_name='haomo.hidelivery.CameraCompressDataPb.video_stamp', index=8,
      number=9, type=4, cpp_type=4, label=3,
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
  serialized_start=317,
  serialized_end=585,
)


_CAMERASIGDATAPB = _descriptor.Descriptor(
  name='CameraSigDataPb',
  full_name='haomo.hidelivery.CameraSigDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CameraSigDataPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.CameraSigDataPb.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='haomo.hidelivery.CameraSigDataPb.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=587,
  serialized_end=677,
)


_CAMERANULLDATAPB = _descriptor.Descriptor(
  name='CameraNullDataPb',
  full_name='haomo.hidelivery.CameraNullDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.CameraNullDataPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=679,
  serialized_end=733,
)

_CAMERADATAPB.fields_by_name['header'].message_type = header__pb2._HEADER
_CAMERADATAPB.fields_by_name['color_space'].enum_type = _COLORSPACE
_CAMERADATAPB.fields_by_name['compress_type'].enum_type = _COMPRESSTYPE
_CAMERACOMPRESSDATAPB.fields_by_name['header'].message_type = header__pb2._HEADER
_CAMERACOMPRESSDATAPB.fields_by_name['color_space'].enum_type = _COLORSPACE
_CAMERACOMPRESSDATAPB.fields_by_name['compress_type'].enum_type = _COMPRESSTYPE
_CAMERASIGDATAPB.fields_by_name['header'].message_type = header__pb2._HEADER
_CAMERANULLDATAPB.fields_by_name['header'].message_type = header__pb2._HEADER
DESCRIPTOR.message_types_by_name['CameraDataPb'] = _CAMERADATAPB
DESCRIPTOR.message_types_by_name['CameraCompressDataPb'] = _CAMERACOMPRESSDATAPB
DESCRIPTOR.message_types_by_name['CameraSigDataPb'] = _CAMERASIGDATAPB
DESCRIPTOR.message_types_by_name['CameraNullDataPb'] = _CAMERANULLDATAPB
DESCRIPTOR.enum_types_by_name['ColorSpace'] = _COLORSPACE
DESCRIPTOR.enum_types_by_name['CompressType'] = _COMPRESSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraDataPb = _reflection.GeneratedProtocolMessageType('CameraDataPb', (_message.Message,), {
  'DESCRIPTOR' : _CAMERADATAPB,
  '__module__' : 'camera_data_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CameraDataPb)
  })
_sym_db.RegisterMessage(CameraDataPb)

CameraCompressDataPb = _reflection.GeneratedProtocolMessageType('CameraCompressDataPb', (_message.Message,), {
  'DESCRIPTOR' : _CAMERACOMPRESSDATAPB,
  '__module__' : 'camera_data_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CameraCompressDataPb)
  })
_sym_db.RegisterMessage(CameraCompressDataPb)

CameraSigDataPb = _reflection.GeneratedProtocolMessageType('CameraSigDataPb', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASIGDATAPB,
  '__module__' : 'camera_data_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CameraSigDataPb)
  })
_sym_db.RegisterMessage(CameraSigDataPb)

CameraNullDataPb = _reflection.GeneratedProtocolMessageType('CameraNullDataPb', (_message.Message,), {
  'DESCRIPTOR' : _CAMERANULLDATAPB,
  '__module__' : 'camera_data_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.CameraNullDataPb)
  })
_sym_db.RegisterMessage(CameraNullDataPb)


# @@protoc_insertion_point(module_scope)