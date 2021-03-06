# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: point_cloud.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='point_cloud.proto',
  package='haomo.hidelivery',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11point_cloud.proto\x12\x10haomo.hidelivery\x1a\x0cheader.proto\"\xcc\x03\n\x10PointCloudDataPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12:\n\x05point\x18\x03 \x03(\x0b\x32+.haomo.hidelivery.PointCloudDataPb.PointPCL\x12\x17\n\x0flidar_current_a\x18\x04 \x01(\x01\x12\x14\n\x0clidar_volt_v\x18\x05 \x01(\x01\x1a\x9c\x01\n\x08PointPCL\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\x11\n\tintensity\x18\x05 \x01(\r\x12\r\n\x05\x63olor\x18\x06 \x01(\r\x12:\n\x04name\x18\x07 \x01(\x0e\x32,.haomo.hidelivery.PointCloudDataPb.LidarName\"u\n\tLidarName\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0b\x46RONT_LIDAR\x10\x01\x12\x14\n\x10\x46RONT_LEFT_LIDAR\x10\x02\x12\x15\n\x11\x46RONT_RIGHT_LIDAR\x10\x03\x12\x0e\n\nREAR_LIDAR\x10\x04\x12\x10\n\x0cMIDDLE_LIDAR\x10\x05\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])



_POINTCLOUDDATAPB_LIDARNAME = _descriptor.EnumDescriptor(
  name='LidarName',
  full_name='haomo.hidelivery.PointCloudDataPb.LidarName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRONT_LIDAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRONT_LEFT_LIDAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRONT_RIGHT_LIDAR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REAR_LIDAR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_LIDAR', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=397,
  serialized_end=514,
)
_sym_db.RegisterEnumDescriptor(_POINTCLOUDDATAPB_LIDARNAME)


_POINTCLOUDDATAPB_POINTPCL = _descriptor.Descriptor(
  name='PointPCL',
  full_name='haomo.hidelivery.PointCloudDataPb.PointPCL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intensity', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.intensity', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.color', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='haomo.hidelivery.PointCloudDataPb.PointPCL.name', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_start=239,
  serialized_end=395,
)

_POINTCLOUDDATAPB = _descriptor.Descriptor(
  name='PointCloudDataPb',
  full_name='haomo.hidelivery.PointCloudDataPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.PointCloudDataPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.PointCloudDataPb.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point', full_name='haomo.hidelivery.PointCloudDataPb.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lidar_current_a', full_name='haomo.hidelivery.PointCloudDataPb.lidar_current_a', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lidar_volt_v', full_name='haomo.hidelivery.PointCloudDataPb.lidar_volt_v', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POINTCLOUDDATAPB_POINTPCL, ],
  enum_types=[
    _POINTCLOUDDATAPB_LIDARNAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=514,
)

_POINTCLOUDDATAPB_POINTPCL.fields_by_name['name'].enum_type = _POINTCLOUDDATAPB_LIDARNAME
_POINTCLOUDDATAPB_POINTPCL.containing_type = _POINTCLOUDDATAPB
_POINTCLOUDDATAPB.fields_by_name['header'].message_type = header__pb2._HEADER
_POINTCLOUDDATAPB.fields_by_name['point'].message_type = _POINTCLOUDDATAPB_POINTPCL
_POINTCLOUDDATAPB_LIDARNAME.containing_type = _POINTCLOUDDATAPB
DESCRIPTOR.message_types_by_name['PointCloudDataPb'] = _POINTCLOUDDATAPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PointCloudDataPb = _reflection.GeneratedProtocolMessageType('PointCloudDataPb', (_message.Message,), {

  'PointPCL' : _reflection.GeneratedProtocolMessageType('PointPCL', (_message.Message,), {
    'DESCRIPTOR' : _POINTCLOUDDATAPB_POINTPCL,
    '__module__' : 'point_cloud_pb2'
    # @@protoc_insertion_point(class_scope:haomo.hidelivery.PointCloudDataPb.PointPCL)
    })
  ,
  'DESCRIPTOR' : _POINTCLOUDDATAPB,
  '__module__' : 'point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.PointCloudDataPb)
  })
_sym_db.RegisterMessage(PointCloudDataPb)
_sym_db.RegisterMessage(PointCloudDataPb.PointPCL)


# @@protoc_insertion_point(module_scope)
