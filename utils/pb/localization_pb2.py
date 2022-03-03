# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: localization.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='localization.proto',
  package='haomo.hidelivery.localization',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12localization.proto\x12\x1dhaomo.hidelivery.localization\x1a\x0cheader.proto\x1a\x0c\x63ommon.proto\"\xf6\x04\n\x04Pose\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12#\n\x08position\x18\x03 \x01(\x0b\x32\x11.haomo.hios.Vec3d\x12#\n\x08velocity\x18\x04 \x01(\x0b\x32\x11.haomo.hios.Vec3d\x12\'\n\x0crotation_rpy\x18\x05 \x01(\x0b\x32\x11.haomo.hios.Vec3d\x12(\n\x08\x61ttitude\x18\x06 \x01(\x0b\x32\x16.haomo.hios.Quaternion\x12\'\n\x0c\x61\x63\x63\x65leration\x18\x07 \x01(\x0b\x32\x11.haomo.hios.Vec3d\x12%\n\nangle_rate\x18\x08 \x01(\x0b\x32\x11.haomo.hios.Vec3d\x12>\n\x06status\x18\t \x01(\x0e\x32..haomo.hidelivery.localization.Pose.StatusType\x12\x11\n\tlongitude\x18\n \x01(\x01\x12\x10\n\x08latitude\x18\x0b \x01(\x01\x12\x0e\n\x06height\x18\x0c \x01(\x01\x12\x14\n\x0cr_horizontal\x18\r \x01(\x01\x12\x16\n\x0er_longitudinal\x18\x0e \x01(\x01\x12\x0f\n\x07link_id\x18\x0f \x03(\t\x12\x0f\n\x07lane_id\x18\x10 \x03(\t\x12\x16\n\x0e\x62\x61se_longitude\x18\x11 \x01(\x01\x12\x15\n\rbase_latitude\x18\x12 \x01(\x01\x12\x13\n\x0b\x62\x61se_height\x18\x13 \x01(\x01\x12\x11\n\tdiagnosis\x18\x14 \x01(\t\",\n\nStatusType\x12\x0c\n\x08NOT_WORK\x10\x00\x12\x08\n\x04INIT\x10\x01\x12\x06\n\x02OK\x10\x02\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])



_POSE_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='haomo.hidelivery.localization.Pose.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_WORK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INIT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=668,
  serialized_end=712,
)
_sym_db.RegisterEnumDescriptor(_POSE_STATUSTYPE)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='haomo.hidelivery.localization.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.localization.Pose.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.localization.Pose.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='haomo.hidelivery.localization.Pose.position', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='haomo.hidelivery.localization.Pose.velocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_rpy', full_name='haomo.hidelivery.localization.Pose.rotation_rpy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attitude', full_name='haomo.hidelivery.localization.Pose.attitude', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='haomo.hidelivery.localization.Pose.acceleration', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle_rate', full_name='haomo.hidelivery.localization.Pose.angle_rate', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='haomo.hidelivery.localization.Pose.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='haomo.hidelivery.localization.Pose.longitude', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='haomo.hidelivery.localization.Pose.latitude', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='haomo.hidelivery.localization.Pose.height', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_horizontal', full_name='haomo.hidelivery.localization.Pose.r_horizontal', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_longitudinal', full_name='haomo.hidelivery.localization.Pose.r_longitudinal', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_id', full_name='haomo.hidelivery.localization.Pose.link_id', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='haomo.hidelivery.localization.Pose.lane_id', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_longitude', full_name='haomo.hidelivery.localization.Pose.base_longitude', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_latitude', full_name='haomo.hidelivery.localization.Pose.base_latitude', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_height', full_name='haomo.hidelivery.localization.Pose.base_height', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diagnosis', full_name='haomo.hidelivery.localization.Pose.diagnosis', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POSE_STATUSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=712,
)

_POSE.fields_by_name['header'].message_type = header__pb2._HEADER
_POSE.fields_by_name['position'].message_type = common__pb2._VEC3D
_POSE.fields_by_name['velocity'].message_type = common__pb2._VEC3D
_POSE.fields_by_name['rotation_rpy'].message_type = common__pb2._VEC3D
_POSE.fields_by_name['attitude'].message_type = common__pb2._QUATERNION
_POSE.fields_by_name['acceleration'].message_type = common__pb2._VEC3D
_POSE.fields_by_name['angle_rate'].message_type = common__pb2._VEC3D
_POSE.fields_by_name['status'].enum_type = _POSE_STATUSTYPE
_POSE_STATUSTYPE.containing_type = _POSE
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'localization_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.localization.Pose)
  })
_sym_db.RegisterMessage(Pose)


# @@protoc_insertion_point(module_scope)