# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: objectfusion.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='objectfusion.proto',
  package='haomo.hipilot',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12objectfusion.proto\x12\rhaomo.hipilot\"\xe2\x07\n\x06OFMObj\x12\x18\n\x10Object_Timestamp\x18\x01 \x01(\r\x12\x12\n\nObject_Num\x18\x02 \x01(\r\x12\x1e\n\x16Object_EyeQ3_Blocked_b\x18\x03 \x01(\x08\x12\x1c\n\x14Object_MRR_Blocked_b\x18\x04 \x01(\x08\x12\x1d\n\x15Object_CRLe_Blocked_b\x18\x05 \x01(\x08\x12\x1d\n\x15Object_CRRi_Blocked_b\x18\x06 \x01(\x08\x12\x1f\n\x17Object_RSDSLe_Blocked_b\x18\x07 \x01(\x08\x12\x1f\n\x17Object_RSDSRi_Blocked_b\x18\x08 \x01(\x08\x12\x17\n\x0fObject_Fus_Type\x18\t \x03(\r\x12\x11\n\tObject_ID\x18\n \x03(\r\x12\x13\n\x0bObject_Type\x18\x0b \x03(\r\x12\x15\n\rObject_Length\x18\x0c \x03(\x02\x12\x14\n\x0cObject_Width\x18\r \x03(\x02\x12\x14\n\x0cObject_Hight\x18\x0e \x03(\x02\x12\x1b\n\x13Object_HeadingAngle\x18\x0f \x03(\x02\x12\x17\n\x0fObject_YawAngle\x18\x10 \x03(\x02\x12\x1a\n\x12Object_MovingState\x18\x11 \x03(\r\x12\x1a\n\x12Object_Orientation\x18\x12 \x03(\r\x12\x11\n\tObject_DX\x18\x13 \x03(\x02\x12\x11\n\tObject_DY\x18\x14 \x03(\x02\x12\x11\n\tObject_VX\x18\x15 \x03(\x02\x12\x11\n\tObject_VY\x18\x16 \x03(\x02\x12\x15\n\rObject_Std_AX\x18\x17 \x03(\x02\x12\x15\n\rObject_Std_AY\x18\x18 \x03(\x02\x12\x15\n\rObject_Std_DX\x18\x19 \x03(\x02\x12\x15\n\rObject_Std_DY\x18\x1a \x03(\x02\x12\x15\n\rObject_Std_VX\x18\x1b \x03(\x02\x12\x15\n\rObject_Std_VY\x18\x1c \x03(\x02\x12\x11\n\tObject_AX\x18\x1d \x03(\x02\x12\x11\n\tObject_AY\x18\x1e \x03(\x02\x12\x19\n\x11Object_Std_Length\x18\x1f \x03(\x02\x12\x18\n\x10Object_Std_Width\x18  \x03(\x02\x12\x1f\n\x17Object_Std_HeadingAngle\x18! \x03(\x02\x12\x18\n\x10Object_Type_Prob\x18\" \x03(\x02\x12\x18\n\x10Object_ExistProb\x18# \x03(\x02\x12\x1b\n\x13Object_ObstacleProb\x18$ \x03(\x02\x12\x12\n\nObject_Age\x18% \x03(\r\x12\x15\n\rObject_Abs_VX\x18& \x03(\x02\x12\x15\n\rObject_Abs_VY\x18\' \x03(\x02\x12\x15\n\rObject_Gantry\x18( \x03(\x08\x62\x06proto3'
)




_OFMOBJ = _descriptor.Descriptor(
  name='OFMObj',
  full_name='haomo.hipilot.OFMObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Object_Timestamp', full_name='haomo.hipilot.OFMObj.Object_Timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Num', full_name='haomo.hipilot.OFMObj.Object_Num', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_EyeQ3_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_EyeQ3_Blocked_b', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_MRR_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_MRR_Blocked_b', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_CRLe_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_CRLe_Blocked_b', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_CRRi_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_CRRi_Blocked_b', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_RSDSLe_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_RSDSLe_Blocked_b', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_RSDSRi_Blocked_b', full_name='haomo.hipilot.OFMObj.Object_RSDSRi_Blocked_b', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Fus_Type', full_name='haomo.hipilot.OFMObj.Object_Fus_Type', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_ID', full_name='haomo.hipilot.OFMObj.Object_ID', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Type', full_name='haomo.hipilot.OFMObj.Object_Type', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Length', full_name='haomo.hipilot.OFMObj.Object_Length', index=11,
      number=12, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Width', full_name='haomo.hipilot.OFMObj.Object_Width', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Hight', full_name='haomo.hipilot.OFMObj.Object_Hight', index=13,
      number=14, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_HeadingAngle', full_name='haomo.hipilot.OFMObj.Object_HeadingAngle', index=14,
      number=15, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_YawAngle', full_name='haomo.hipilot.OFMObj.Object_YawAngle', index=15,
      number=16, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_MovingState', full_name='haomo.hipilot.OFMObj.Object_MovingState', index=16,
      number=17, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Orientation', full_name='haomo.hipilot.OFMObj.Object_Orientation', index=17,
      number=18, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_DX', full_name='haomo.hipilot.OFMObj.Object_DX', index=18,
      number=19, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_DY', full_name='haomo.hipilot.OFMObj.Object_DY', index=19,
      number=20, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_VX', full_name='haomo.hipilot.OFMObj.Object_VX', index=20,
      number=21, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_VY', full_name='haomo.hipilot.OFMObj.Object_VY', index=21,
      number=22, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_AX', full_name='haomo.hipilot.OFMObj.Object_Std_AX', index=22,
      number=23, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_AY', full_name='haomo.hipilot.OFMObj.Object_Std_AY', index=23,
      number=24, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_DX', full_name='haomo.hipilot.OFMObj.Object_Std_DX', index=24,
      number=25, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_DY', full_name='haomo.hipilot.OFMObj.Object_Std_DY', index=25,
      number=26, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_VX', full_name='haomo.hipilot.OFMObj.Object_Std_VX', index=26,
      number=27, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_VY', full_name='haomo.hipilot.OFMObj.Object_Std_VY', index=27,
      number=28, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_AX', full_name='haomo.hipilot.OFMObj.Object_AX', index=28,
      number=29, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_AY', full_name='haomo.hipilot.OFMObj.Object_AY', index=29,
      number=30, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_Length', full_name='haomo.hipilot.OFMObj.Object_Std_Length', index=30,
      number=31, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_Width', full_name='haomo.hipilot.OFMObj.Object_Std_Width', index=31,
      number=32, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Std_HeadingAngle', full_name='haomo.hipilot.OFMObj.Object_Std_HeadingAngle', index=32,
      number=33, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Type_Prob', full_name='haomo.hipilot.OFMObj.Object_Type_Prob', index=33,
      number=34, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_ExistProb', full_name='haomo.hipilot.OFMObj.Object_ExistProb', index=34,
      number=35, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_ObstacleProb', full_name='haomo.hipilot.OFMObj.Object_ObstacleProb', index=35,
      number=36, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Age', full_name='haomo.hipilot.OFMObj.Object_Age', index=36,
      number=37, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Abs_VX', full_name='haomo.hipilot.OFMObj.Object_Abs_VX', index=37,
      number=38, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Abs_VY', full_name='haomo.hipilot.OFMObj.Object_Abs_VY', index=38,
      number=39, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Object_Gantry', full_name='haomo.hipilot.OFMObj.Object_Gantry', index=39,
      number=40, type=8, cpp_type=7, label=3,
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
  serialized_start=38,
  serialized_end=1032,
)

DESCRIPTOR.message_types_by_name['OFMObj'] = _OFMOBJ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OFMObj = _reflection.GeneratedProtocolMessageType('OFMObj', (_message.Message,), {
  'DESCRIPTOR' : _OFMOBJ,
  '__module__' : 'objectfusion_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hipilot.OFMObj)
  })
_sym_db.RegisterMessage(OFMObj)


# @@protoc_insertion_point(module_scope)
