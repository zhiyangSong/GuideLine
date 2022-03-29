# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rtk_trajectory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import localization_pb2 as localization__pb2
import pnc_point_pb2 as pnc__point__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rtk_trajectory.proto',
  package='haomo.hidelivery.control',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14rtk_trajectory.proto\x12\x18haomo.hidelivery.control\x1a\x12localization.proto\x1a\x0fpnc_point.proto\"\x91\x01\n\rRtkTrajectory\x12;\n\x0ertk_trajectory\x18\x01 \x03(\x0b\x32#.haomo.hidelivery.localization.Pose\x12\x43\n\x0fref_traj_points\x18\x02 \x03(\x0b\x32*.haomo.hidelivery.planning.TrajectoryPointb\x06proto3'
  ,
  dependencies=[localization__pb2.DESCRIPTOR,pnc__point__pb2.DESCRIPTOR,])




_RTKTRAJECTORY = _descriptor.Descriptor(
  name='RtkTrajectory',
  full_name='haomo.hidelivery.control.RtkTrajectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtk_trajectory', full_name='haomo.hidelivery.control.RtkTrajectory.rtk_trajectory', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_traj_points', full_name='haomo.hidelivery.control.RtkTrajectory.ref_traj_points', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=88,
  serialized_end=233,
)

_RTKTRAJECTORY.fields_by_name['rtk_trajectory'].message_type = localization__pb2._POSE
_RTKTRAJECTORY.fields_by_name['ref_traj_points'].message_type = pnc__point__pb2._TRAJECTORYPOINT
DESCRIPTOR.message_types_by_name['RtkTrajectory'] = _RTKTRAJECTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RtkTrajectory = _reflection.GeneratedProtocolMessageType('RtkTrajectory', (_message.Message,), {
  'DESCRIPTOR' : _RTKTRAJECTORY,
  '__module__' : 'rtk_trajectory_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.control.RtkTrajectory)
  })
_sym_db.RegisterMessage(RtkTrajectory)


# @@protoc_insertion_point(module_scope)
