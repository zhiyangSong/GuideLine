# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_speed_control.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import map_geometry_pb2 as map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_speed_control.proto',
  package='haomo.hidelivery.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x17map_speed_control.proto\x12\x16haomo.hidelivery.hdmap\x1a\x12map_geometry.proto\"c\n\x0cSpeedControl\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x07polygon\x18\x02 \x01(\x0b\x32\x1f.haomo.hidelivery.hdmap.Polygon\x12\x13\n\x0bspeed_limit\x18\x03 \x01(\x01\"L\n\rSpeedControls\x12;\n\rspeed_control\x18\x01 \x03(\x0b\x32$.haomo.hidelivery.hdmap.SpeedControl'
  ,
  dependencies=[map__geometry__pb2.DESCRIPTOR,])




_SPEEDCONTROL = _descriptor.Descriptor(
  name='SpeedControl',
  full_name='haomo.hidelivery.hdmap.SpeedControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='haomo.hidelivery.hdmap.SpeedControl.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='haomo.hidelivery.hdmap.SpeedControl.polygon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='haomo.hidelivery.hdmap.SpeedControl.speed_limit', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=170,
)


_SPEEDCONTROLS = _descriptor.Descriptor(
  name='SpeedControls',
  full_name='haomo.hidelivery.hdmap.SpeedControls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed_control', full_name='haomo.hidelivery.hdmap.SpeedControls.speed_control', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=248,
)

_SPEEDCONTROL.fields_by_name['polygon'].message_type = map__geometry__pb2._POLYGON
_SPEEDCONTROLS.fields_by_name['speed_control'].message_type = _SPEEDCONTROL
DESCRIPTOR.message_types_by_name['SpeedControl'] = _SPEEDCONTROL
DESCRIPTOR.message_types_by_name['SpeedControls'] = _SPEEDCONTROLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpeedControl = _reflection.GeneratedProtocolMessageType('SpeedControl', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDCONTROL,
  '__module__' : 'map_speed_control_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.hdmap.SpeedControl)
  })
_sym_db.RegisterMessage(SpeedControl)

SpeedControls = _reflection.GeneratedProtocolMessageType('SpeedControls', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDCONTROLS,
  '__module__' : 'map_speed_control_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.hdmap.SpeedControls)
  })
_sym_db.RegisterMessage(SpeedControls)


# @@protoc_insertion_point(module_scope)
