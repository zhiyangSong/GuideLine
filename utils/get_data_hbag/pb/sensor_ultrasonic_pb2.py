# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_ultrasonic.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_ultrasonic.proto',
  package='haomo.hidelivery',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x17sensor_ultrasonic.proto\x12\x10haomo.hidelivery\x1a\x0cheader.proto\"M\n\x0eUltrasonicEcho\x12\x0f\n\x07\x65\x63ho_id\x18\x01 \x01(\x05\x12\r\n\x05range\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\x12\x0c\n\x04peak\x18\x04 \x01(\x01\"\x95\x03\n\x0fUltrasonicProbe\x12\x12\n\nsensor_pos\x18\x01 \x01(\x05\x12\x14\n\x0c\x65\x63hoes_count\x18\x02 \x01(\x05\x12\x11\n\tring_time\x18\x03 \x01(\x01\x12\x30\n\x06\x65\x63hoes\x18\x04 \x03(\x0b\x32 .haomo.hidelivery.UltrasonicEcho\x12\x19\n\x11signal_source_pos\x18\x05 \x01(\x05\x12\x32\n\x06status\x18\x06 \x01(\x0e\x32\".haomo.hidelivery.UltrasonicStatus\x12\x13\n\x0b\x66ilter_dist\x18\x07 \x01(\x01\x12\x11\n\tamplitude\x18\x08 \x01(\x01\x12\x35\n\nnoise_type\x18\t \x01(\x0e\x32!.haomo.hidelivery.UltrasonicNoise\x12\x1b\n\x13is_first_echo_valid\x18\n \x01(\x08\x12\x12\n\nnew_status\x18\x0b \x01(\x05\x12\x16\n\x0enew_noise_type\x18\x0c \x01(\x05\x12\r\n\x05wnull\x18\r \x01(\x05\x12\r\n\x05\x63null\x18\x0e \x01(\x05\"\xcb\x01\n\x12Ultraosnic_SendRev\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x34\n\ttx_probes\x18\x02 \x01(\x0b\x32!.haomo.hidelivery.UltrasonicProbe\x12\x35\n\nrx0_probes\x18\x03 \x01(\x0b\x32!.haomo.hidelivery.UltrasonicProbe\x12\x35\n\nrx1_probes\x18\x04 \x01(\x0b\x32!.haomo.hidelivery.UltrasonicProbe\"\xf2\x01\n\rUltrasonicPkg\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x13\n\x0bsys_time_us\x18\x02 \x01(\x04\x12<\n\x0eultrasonic_msg\x18\x03 \x03(\x0b\x32$.haomo.hidelivery.Ultraosnic_SendRev\x12\x15\n\rpa_work_state\x18\x04 \x01(\r\x12\x15\n\rdisable_cause\x18\x05 \x01(\r\x12\x13\n\x0brooling_cnt\x18\x06 \x01(\r\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\x08\x12\x15\n\rmcu_send_time\x18\x08 \x01(\x04\"\xf7\x02\n\rUltrasonicinf\x12\r\n\x05\x66rs_x\x18\x01 \x01(\x02\x12\r\n\x05\x66rs_y\x18\x02 \x01(\x02\x12\r\n\x05\x66ls_x\x18\x03 \x01(\x02\x12\r\n\x05\x66ls_y\x18\x04 \x01(\x02\x12\r\n\x05rrs_x\x18\x05 \x01(\x02\x12\r\n\x05rrs_y\x18\x06 \x01(\x02\x12\r\n\x05rls_x\x18\x07 \x01(\x02\x12\r\n\x05rls_y\x18\x08 \x01(\x02\x12\r\n\x05\x66rc_x\x18\t \x01(\x02\x12\r\n\x05\x66rc_y\x18\n \x01(\x02\x12\r\n\x05\x66rm_x\x18\x0b \x01(\x02\x12\r\n\x05\x66rm_y\x18\x0c \x01(\x02\x12\r\n\x05\x66lc_x\x18\r \x01(\x02\x12\r\n\x05\x66lc_y\x18\x0e \x01(\x02\x12\r\n\x05\x66lm_x\x18\x0f \x01(\x02\x12\r\n\x05\x66lm_y\x18\x10 \x01(\x02\x12\r\n\x05rrc_x\x18\x11 \x01(\x02\x12\r\n\x05rrc_y\x18\x12 \x01(\x02\x12\r\n\x05rrm_x\x18\x13 \x01(\x02\x12\r\n\x05rrm_y\x18\x14 \x01(\x02\x12\r\n\x05rlc_x\x18\x15 \x01(\x02\x12\r\n\x05rlc_y\x18\x16 \x01(\x02\x12\r\n\x05rlm_x\x18\x17 \x01(\x02\x12\r\n\x05rlm_y\x18\x18 \x01(\x02\"k\n\x10UltrasonicInfoPb\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12\x33\n\nultra_info\x18\x02 \x01(\x0b\x32\x1f.haomo.hidelivery.Ultrasonicinf*`\n\x0fUltrasonicNoise\x12\x06\n\x02NO\x10\x00\x12\x15\n\x11\x41\x44J_VECHILE_NOISE\x10\x01\x12\n\n\x06SLIGHT\x10\x02\x12\t\n\x05HEAVY\x10\x03\x12\x17\n\x12UNKNOWN_NOISE_TYPE\x10\xff\x01*A\n\x10UltrasonicStatus\x12\n\n\x06NORMAL\x10\x00\x12\x0c\n\x08\x41\x42NORMAL\x10\x01\x12\x13\n\x0eUNKNOWN_STATUS\x10\xff\x01\x62\x06proto3'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])

_ULTRASONICNOISE = _descriptor.EnumDescriptor(
  name='UltrasonicNoise',
  full_name='haomo.hidelivery.UltrasonicNoise',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADJ_VECHILE_NOISE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLIGHT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAVY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_NOISE_TYPE', index=4, number=255,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1484,
  serialized_end=1580,
)
_sym_db.RegisterEnumDescriptor(_ULTRASONICNOISE)

UltrasonicNoise = enum_type_wrapper.EnumTypeWrapper(_ULTRASONICNOISE)
_ULTRASONICSTATUS = _descriptor.EnumDescriptor(
  name='UltrasonicStatus',
  full_name='haomo.hidelivery.UltrasonicStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABNORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_STATUS', index=2, number=255,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1582,
  serialized_end=1647,
)
_sym_db.RegisterEnumDescriptor(_ULTRASONICSTATUS)

UltrasonicStatus = enum_type_wrapper.EnumTypeWrapper(_ULTRASONICSTATUS)
NO = 0
ADJ_VECHILE_NOISE = 1
SLIGHT = 2
HEAVY = 3
UNKNOWN_NOISE_TYPE = 255
NORMAL = 0
ABNORMAL = 1
UNKNOWN_STATUS = 255



_ULTRASONICECHO = _descriptor.Descriptor(
  name='UltrasonicEcho',
  full_name='haomo.hidelivery.UltrasonicEcho',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='echo_id', full_name='haomo.hidelivery.UltrasonicEcho.echo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='haomo.hidelivery.UltrasonicEcho.range', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='haomo.hidelivery.UltrasonicEcho.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak', full_name='haomo.hidelivery.UltrasonicEcho.peak', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=59,
  serialized_end=136,
)


_ULTRASONICPROBE = _descriptor.Descriptor(
  name='UltrasonicProbe',
  full_name='haomo.hidelivery.UltrasonicProbe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_pos', full_name='haomo.hidelivery.UltrasonicProbe.sensor_pos', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='echoes_count', full_name='haomo.hidelivery.UltrasonicProbe.echoes_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ring_time', full_name='haomo.hidelivery.UltrasonicProbe.ring_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='echoes', full_name='haomo.hidelivery.UltrasonicProbe.echoes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signal_source_pos', full_name='haomo.hidelivery.UltrasonicProbe.signal_source_pos', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='haomo.hidelivery.UltrasonicProbe.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_dist', full_name='haomo.hidelivery.UltrasonicProbe.filter_dist', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amplitude', full_name='haomo.hidelivery.UltrasonicProbe.amplitude', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='noise_type', full_name='haomo.hidelivery.UltrasonicProbe.noise_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_first_echo_valid', full_name='haomo.hidelivery.UltrasonicProbe.is_first_echo_valid', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_status', full_name='haomo.hidelivery.UltrasonicProbe.new_status', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_noise_type', full_name='haomo.hidelivery.UltrasonicProbe.new_noise_type', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wnull', full_name='haomo.hidelivery.UltrasonicProbe.wnull', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnull', full_name='haomo.hidelivery.UltrasonicProbe.cnull', index=13,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=139,
  serialized_end=544,
)


_ULTRAOSNIC_SENDREV = _descriptor.Descriptor(
  name='Ultraosnic_SendRev',
  full_name='haomo.hidelivery.Ultraosnic_SendRev',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='haomo.hidelivery.Ultraosnic_SendRev.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_probes', full_name='haomo.hidelivery.Ultraosnic_SendRev.tx_probes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx0_probes', full_name='haomo.hidelivery.Ultraosnic_SendRev.rx0_probes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx1_probes', full_name='haomo.hidelivery.Ultraosnic_SendRev.rx1_probes', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=547,
  serialized_end=750,
)


_ULTRASONICPKG = _descriptor.Descriptor(
  name='UltrasonicPkg',
  full_name='haomo.hidelivery.UltrasonicPkg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.UltrasonicPkg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_time_us', full_name='haomo.hidelivery.UltrasonicPkg.sys_time_us', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ultrasonic_msg', full_name='haomo.hidelivery.UltrasonicPkg.ultrasonic_msg', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pa_work_state', full_name='haomo.hidelivery.UltrasonicPkg.pa_work_state', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_cause', full_name='haomo.hidelivery.UltrasonicPkg.disable_cause', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rooling_cnt', full_name='haomo.hidelivery.UltrasonicPkg.rooling_cnt', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='haomo.hidelivery.UltrasonicPkg.checksum', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mcu_send_time', full_name='haomo.hidelivery.UltrasonicPkg.mcu_send_time', index=7,
      number=8, type=4, cpp_type=4, label=1,
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
  serialized_start=753,
  serialized_end=995,
)


_ULTRASONICINF = _descriptor.Descriptor(
  name='Ultrasonicinf',
  full_name='haomo.hidelivery.Ultrasonicinf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frs_x', full_name='haomo.hidelivery.Ultrasonicinf.frs_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frs_y', full_name='haomo.hidelivery.Ultrasonicinf.frs_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fls_x', full_name='haomo.hidelivery.Ultrasonicinf.fls_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fls_y', full_name='haomo.hidelivery.Ultrasonicinf.fls_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrs_x', full_name='haomo.hidelivery.Ultrasonicinf.rrs_x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrs_y', full_name='haomo.hidelivery.Ultrasonicinf.rrs_y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rls_x', full_name='haomo.hidelivery.Ultrasonicinf.rls_x', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rls_y', full_name='haomo.hidelivery.Ultrasonicinf.rls_y', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frc_x', full_name='haomo.hidelivery.Ultrasonicinf.frc_x', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frc_y', full_name='haomo.hidelivery.Ultrasonicinf.frc_y', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frm_x', full_name='haomo.hidelivery.Ultrasonicinf.frm_x', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frm_y', full_name='haomo.hidelivery.Ultrasonicinf.frm_y', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flc_x', full_name='haomo.hidelivery.Ultrasonicinf.flc_x', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flc_y', full_name='haomo.hidelivery.Ultrasonicinf.flc_y', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flm_x', full_name='haomo.hidelivery.Ultrasonicinf.flm_x', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flm_y', full_name='haomo.hidelivery.Ultrasonicinf.flm_y', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrc_x', full_name='haomo.hidelivery.Ultrasonicinf.rrc_x', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrc_y', full_name='haomo.hidelivery.Ultrasonicinf.rrc_y', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrm_x', full_name='haomo.hidelivery.Ultrasonicinf.rrm_x', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rrm_y', full_name='haomo.hidelivery.Ultrasonicinf.rrm_y', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rlc_x', full_name='haomo.hidelivery.Ultrasonicinf.rlc_x', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rlc_y', full_name='haomo.hidelivery.Ultrasonicinf.rlc_y', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rlm_x', full_name='haomo.hidelivery.Ultrasonicinf.rlm_x', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rlm_y', full_name='haomo.hidelivery.Ultrasonicinf.rlm_y', index=23,
      number=24, type=2, cpp_type=6, label=1,
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
  serialized_start=998,
  serialized_end=1373,
)


_ULTRASONICINFOPB = _descriptor.Descriptor(
  name='UltrasonicInfoPb',
  full_name='haomo.hidelivery.UltrasonicInfoPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.UltrasonicInfoPb.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ultra_info', full_name='haomo.hidelivery.UltrasonicInfoPb.ultra_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1375,
  serialized_end=1482,
)

_ULTRASONICPROBE.fields_by_name['echoes'].message_type = _ULTRASONICECHO
_ULTRASONICPROBE.fields_by_name['status'].enum_type = _ULTRASONICSTATUS
_ULTRASONICPROBE.fields_by_name['noise_type'].enum_type = _ULTRASONICNOISE
_ULTRAOSNIC_SENDREV.fields_by_name['tx_probes'].message_type = _ULTRASONICPROBE
_ULTRAOSNIC_SENDREV.fields_by_name['rx0_probes'].message_type = _ULTRASONICPROBE
_ULTRAOSNIC_SENDREV.fields_by_name['rx1_probes'].message_type = _ULTRASONICPROBE
_ULTRASONICPKG.fields_by_name['header'].message_type = header__pb2._HEADER
_ULTRASONICPKG.fields_by_name['ultrasonic_msg'].message_type = _ULTRAOSNIC_SENDREV
_ULTRASONICINFOPB.fields_by_name['header'].message_type = header__pb2._HEADER
_ULTRASONICINFOPB.fields_by_name['ultra_info'].message_type = _ULTRASONICINF
DESCRIPTOR.message_types_by_name['UltrasonicEcho'] = _ULTRASONICECHO
DESCRIPTOR.message_types_by_name['UltrasonicProbe'] = _ULTRASONICPROBE
DESCRIPTOR.message_types_by_name['Ultraosnic_SendRev'] = _ULTRAOSNIC_SENDREV
DESCRIPTOR.message_types_by_name['UltrasonicPkg'] = _ULTRASONICPKG
DESCRIPTOR.message_types_by_name['Ultrasonicinf'] = _ULTRASONICINF
DESCRIPTOR.message_types_by_name['UltrasonicInfoPb'] = _ULTRASONICINFOPB
DESCRIPTOR.enum_types_by_name['UltrasonicNoise'] = _ULTRASONICNOISE
DESCRIPTOR.enum_types_by_name['UltrasonicStatus'] = _ULTRASONICSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UltrasonicEcho = _reflection.GeneratedProtocolMessageType('UltrasonicEcho', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICECHO,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.UltrasonicEcho)
  })
_sym_db.RegisterMessage(UltrasonicEcho)

UltrasonicProbe = _reflection.GeneratedProtocolMessageType('UltrasonicProbe', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICPROBE,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.UltrasonicProbe)
  })
_sym_db.RegisterMessage(UltrasonicProbe)

Ultraosnic_SendRev = _reflection.GeneratedProtocolMessageType('Ultraosnic_SendRev', (_message.Message,), {
  'DESCRIPTOR' : _ULTRAOSNIC_SENDREV,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.Ultraosnic_SendRev)
  })
_sym_db.RegisterMessage(Ultraosnic_SendRev)

UltrasonicPkg = _reflection.GeneratedProtocolMessageType('UltrasonicPkg', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICPKG,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.UltrasonicPkg)
  })
_sym_db.RegisterMessage(UltrasonicPkg)

Ultrasonicinf = _reflection.GeneratedProtocolMessageType('Ultrasonicinf', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICINF,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.Ultrasonicinf)
  })
_sym_db.RegisterMessage(Ultrasonicinf)

UltrasonicInfoPb = _reflection.GeneratedProtocolMessageType('UltrasonicInfoPb', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONICINFOPB,
  '__module__' : 'sensor_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.UltrasonicInfoPb)
  })
_sym_db.RegisterMessage(UltrasonicInfoPb)


# @@protoc_insertion_point(module_scope)
