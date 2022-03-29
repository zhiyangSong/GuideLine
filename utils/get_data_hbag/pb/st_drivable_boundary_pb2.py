# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: st_drivable_boundary.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='st_drivable_boundary.proto',
  package='haomo.hidelivery.planning',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1ast_drivable_boundary.proto\x12\x19haomo.hidelivery.planning\"s\n\x1aSTDrivableBoundaryInstance\x12\t\n\x01t\x18\x01 \x01(\x01\x12\x0f\n\x07s_lower\x18\x02 \x01(\x01\x12\x0f\n\x07s_upper\x18\x03 \x01(\x01\x12\x13\n\x0bv_obs_lower\x18\x04 \x01(\x01\x12\x13\n\x0bv_obs_upper\x18\x05 \x01(\x01\"`\n\x12STDrivableBoundary\x12J\n\x0bst_boundary\x18\x01 \x03(\x0b\x32\x35.haomo.hidelivery.planning.STDrivableBoundaryInstanceb\x06proto3'
)




_STDRIVABLEBOUNDARYINSTANCE = _descriptor.Descriptor(
  name='STDrivableBoundaryInstance',
  full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='t', full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance.t', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s_lower', full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance.s_lower', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s_upper', full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance.s_upper', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v_obs_lower', full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance.v_obs_lower', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v_obs_upper', full_name='haomo.hidelivery.planning.STDrivableBoundaryInstance.v_obs_upper', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=172,
)


_STDRIVABLEBOUNDARY = _descriptor.Descriptor(
  name='STDrivableBoundary',
  full_name='haomo.hidelivery.planning.STDrivableBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='st_boundary', full_name='haomo.hidelivery.planning.STDrivableBoundary.st_boundary', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=270,
)

_STDRIVABLEBOUNDARY.fields_by_name['st_boundary'].message_type = _STDRIVABLEBOUNDARYINSTANCE
DESCRIPTOR.message_types_by_name['STDrivableBoundaryInstance'] = _STDRIVABLEBOUNDARYINSTANCE
DESCRIPTOR.message_types_by_name['STDrivableBoundary'] = _STDRIVABLEBOUNDARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

STDrivableBoundaryInstance = _reflection.GeneratedProtocolMessageType('STDrivableBoundaryInstance', (_message.Message,), {
  'DESCRIPTOR' : _STDRIVABLEBOUNDARYINSTANCE,
  '__module__' : 'st_drivable_boundary_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.planning.STDrivableBoundaryInstance)
  })
_sym_db.RegisterMessage(STDrivableBoundaryInstance)

STDrivableBoundary = _reflection.GeneratedProtocolMessageType('STDrivableBoundary', (_message.Message,), {
  'DESCRIPTOR' : _STDRIVABLEBOUNDARY,
  '__module__' : 'st_drivable_boundary_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.planning.STDrivableBoundary)
  })
_sym_db.RegisterMessage(STDrivableBoundary)


# @@protoc_insertion_point(module_scope)
