# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dms.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dms.proto',
  package='haomo.hios',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tdms.proto\x12\nhaomo.hios\x1a\x0cheader.proto\"\xe2\x05\n\x05\x44MSPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12=\n\x11\x64istraction_level\x18\x03 \x01(\x0e\x32\".haomo.hios.DMSPb.DistractionLevel\x12;\n\x10\x64rowsiness_level\x18\x04 \x01(\x0e\x32!.haomo.hios.DMSPb.DrowsinessLevel\x12/\n\ndms_status\x18\x05 \x01(\x0e\x32\x1b.haomo.hios.DMSPb.DMSStatus\x12-\n\thead_detn\x18\x06 \x01(\x0e\x32\x1a.haomo.hios.DMSPb.HeadDetn\"\x9a\x01\n\x10\x44istractionLevel\x12\x12\n\x0eNO_DISTRACTION\x10\x00\x12\x19\n\x15LOW_LEVEL_DISTRACTION\x10\x01\x12\x1c\n\x18MIDDLE_LEVEL_DISTRACTION\x10\x02\x12\x1a\n\x16HIGH_LEVEL_DISTRACTION\x10\x03\x12\x17\n\x13\x44ISTRACTION_INVALID\x10\x07\"\x04\x08\x04\x10\x06\"\x94\x01\n\x0f\x44rowsinessLevel\x12\x11\n\rNO_DROWSINESS\x10\x00\x12\x18\n\x14LOW_LEVEL_DROWSINESS\x10\x01\x12\x1b\n\x17MIDDLE_LEVEL_DROWSINESS\x10\x02\x12\x19\n\x15HIGH_LEVEL_DROWSINESS\x10\x03\x12\x16\n\x12\x44ROWSINESS_INVALID\x10\x07\"\x04\x08\x04\x10\x06\"[\n\tDMSStatus\x12\r\n\tBLINDNESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0e\n\nNOT_ACTIVE\x10\x03\x12\x12\n\x0e\x44MSSTS_INVALID\x10\x07\"\x04\x08\x04\x10\x06\"3\n\x08HeadDetn\x12\x0f\n\x0bHEADDETN_NO\x10\x00\x12\x10\n\x0cHEADDETN_YES\x10\x01\"\x04\x08\x02\x10\x07\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])



_DMSPB_DISTRACTIONLEVEL = _descriptor.EnumDescriptor(
  name='DistractionLevel',
  full_name='haomo.hios.DMSPb.DistractionLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_DISTRACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_LEVEL_DISTRACTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_LEVEL_DISTRACTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH_LEVEL_DISTRACTION', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTRACTION_INVALID', index=4, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=327,
  serialized_end=481,
)
_sym_db.RegisterEnumDescriptor(_DMSPB_DISTRACTIONLEVEL)

_DMSPB_DROWSINESSLEVEL = _descriptor.EnumDescriptor(
  name='DrowsinessLevel',
  full_name='haomo.hios.DMSPb.DrowsinessLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_DROWSINESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_LEVEL_DROWSINESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_LEVEL_DROWSINESS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH_LEVEL_DROWSINESS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROWSINESS_INVALID', index=4, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=484,
  serialized_end=632,
)
_sym_db.RegisterEnumDescriptor(_DMSPB_DROWSINESSLEVEL)

_DMSPB_DMSSTATUS = _descriptor.EnumDescriptor(
  name='DMSStatus',
  full_name='haomo.hios.DMSPb.DMSStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLINDNESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ACTIVE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DMSSTS_INVALID', index=4, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=634,
  serialized_end=725,
)
_sym_db.RegisterEnumDescriptor(_DMSPB_DMSSTATUS)

_DMSPB_HEADDETN = _descriptor.EnumDescriptor(
  name='HeadDetn',
  full_name='haomo.hios.DMSPb.HeadDetn',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEADDETN_NO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADDETN_YES', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=727,
  serialized_end=778,
)
_sym_db.RegisterEnumDescriptor(_DMSPB_HEADDETN)


_DMSPB = _descriptor.Descriptor(
  name='DMSPb',
  full_name='haomo.hios.DMSPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hios.DMSPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hios.DMSPb.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distraction_level', full_name='haomo.hios.DMSPb.distraction_level', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drowsiness_level', full_name='haomo.hios.DMSPb.drowsiness_level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dms_status', full_name='haomo.hios.DMSPb.dms_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_detn', full_name='haomo.hios.DMSPb.head_detn', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DMSPB_DISTRACTIONLEVEL,
    _DMSPB_DROWSINESSLEVEL,
    _DMSPB_DMSSTATUS,
    _DMSPB_HEADDETN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=778,
)

_DMSPB.fields_by_name['header'].message_type = header__pb2._HEADER
_DMSPB.fields_by_name['distraction_level'].enum_type = _DMSPB_DISTRACTIONLEVEL
_DMSPB.fields_by_name['drowsiness_level'].enum_type = _DMSPB_DROWSINESSLEVEL
_DMSPB.fields_by_name['dms_status'].enum_type = _DMSPB_DMSSTATUS
_DMSPB.fields_by_name['head_detn'].enum_type = _DMSPB_HEADDETN
_DMSPB_DISTRACTIONLEVEL.containing_type = _DMSPB
_DMSPB_DROWSINESSLEVEL.containing_type = _DMSPB
_DMSPB_DMSSTATUS.containing_type = _DMSPB
_DMSPB_HEADDETN.containing_type = _DMSPB
DESCRIPTOR.message_types_by_name['DMSPb'] = _DMSPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DMSPb = _reflection.GeneratedProtocolMessageType('DMSPb', (_message.Message,), {
  'DESCRIPTOR' : _DMSPB,
  '__module__' : 'dms_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hios.DMSPb)
  })
_sym_db.RegisterMessage(DMSPb)


# @@protoc_insertion_point(module_scope)