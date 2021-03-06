# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import map_clear_area_pb2 as map__clear__area__pb2
import map_crosswalk_pb2 as map__crosswalk__pb2
import map_junction_pb2 as map__junction__pb2
import map_lane_pb2 as map__lane__pb2
import map_overlap_pb2 as map__overlap__pb2
import map_signal_pb2 as map__signal__pb2
import map_speed_bump_pb2 as map__speed__bump__pb2
import map_stop_sign_pb2 as map__stop__sign__pb2
import map_yield_sign_pb2 as map__yield__sign__pb2
import map_road_pb2 as map__road__pb2
import map_parking_space_pb2 as map__parking__space__pb2
import map_pnc_junction_pb2 as map__pnc__junction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map.proto',
  package='haomo.hidelivery.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\tmap.proto\x12\x16haomo.hidelivery.hdmap\x1a\x14map_clear_area.proto\x1a\x13map_crosswalk.proto\x1a\x12map_junction.proto\x1a\x0emap_lane.proto\x1a\x11map_overlap.proto\x1a\x10map_signal.proto\x1a\x14map_speed_bump.proto\x1a\x13map_stop_sign.proto\x1a\x14map_yield_sign.proto\x1a\x0emap_road.proto\x1a\x17map_parking_space.proto\x1a\x16map_pnc_junction.proto\"\x1a\n\nProjection\x12\x0c\n\x04proj\x18\x01 \x01(\t\"\xf5\x01\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x0c\x12\x36\n\nprojection\x18\x03 \x01(\x0b\x32\".haomo.hidelivery.hdmap.Projection\x12\x10\n\x08\x64istrict\x18\x04 \x01(\x0c\x12\x12\n\ngeneration\x18\x05 \x01(\x0c\x12\x11\n\trev_major\x18\x06 \x01(\x0c\x12\x11\n\trev_minor\x18\x07 \x01(\x0c\x12\x0c\n\x04left\x18\x08 \x01(\x01\x12\x0b\n\x03top\x18\t \x01(\x01\x12\r\n\x05right\x18\n \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x0b \x01(\x01\x12\x0e\n\x06vendor\x18\x0c \x01(\x0c\"\xa6\x05\n\x03Map\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.haomo.hidelivery.hdmap.Header\x12\x34\n\tcrosswalk\x18\x02 \x03(\x0b\x32!.haomo.hidelivery.hdmap.Crosswalk\x12\x32\n\x08junction\x18\x03 \x03(\x0b\x32 .haomo.hidelivery.hdmap.Junction\x12*\n\x04lane\x18\x04 \x03(\x0b\x32\x1c.haomo.hidelivery.hdmap.Lane\x12\x33\n\tstop_sign\x18\x05 \x03(\x0b\x32 .haomo.hidelivery.hdmap.StopSign\x12.\n\x06signal\x18\x06 \x03(\x0b\x32\x1e.haomo.hidelivery.hdmap.Signal\x12\x30\n\x05yield\x18\x07 \x03(\x0b\x32!.haomo.hidelivery.hdmap.YieldSign\x12\x30\n\x07overlap\x18\x08 \x03(\x0b\x32\x1f.haomo.hidelivery.hdmap.Overlap\x12\x35\n\nclear_area\x18\t \x03(\x0b\x32!.haomo.hidelivery.hdmap.ClearArea\x12\x35\n\nspeed_bump\x18\n \x03(\x0b\x32!.haomo.hidelivery.hdmap.SpeedBump\x12*\n\x04road\x18\x0b \x03(\x0b\x32\x1c.haomo.hidelivery.hdmap.Road\x12;\n\rparking_space\x18\x0c \x03(\x0b\x32$.haomo.hidelivery.hdmap.ParkingSpace\x12\x39\n\x0cpnc_junction\x18\r \x03(\x0b\x32#.haomo.hidelivery.hdmap.PNCJunction'
  ,
  dependencies=[map__clear__area__pb2.DESCRIPTOR,map__crosswalk__pb2.DESCRIPTOR,map__junction__pb2.DESCRIPTOR,map__lane__pb2.DESCRIPTOR,map__overlap__pb2.DESCRIPTOR,map__signal__pb2.DESCRIPTOR,map__speed__bump__pb2.DESCRIPTOR,map__stop__sign__pb2.DESCRIPTOR,map__yield__sign__pb2.DESCRIPTOR,map__road__pb2.DESCRIPTOR,map__parking__space__pb2.DESCRIPTOR,map__pnc__junction__pb2.DESCRIPTOR,])




_PROJECTION = _descriptor.Descriptor(
  name='Projection',
  full_name='haomo.hidelivery.hdmap.Projection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj', full_name='haomo.hidelivery.hdmap.Projection.proj', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=309,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='haomo.hidelivery.hdmap.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='haomo.hidelivery.hdmap.Header.version', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='haomo.hidelivery.hdmap.Header.date', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projection', full_name='haomo.hidelivery.hdmap.Header.projection', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='district', full_name='haomo.hidelivery.hdmap.Header.district', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation', full_name='haomo.hidelivery.hdmap.Header.generation', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rev_major', full_name='haomo.hidelivery.hdmap.Header.rev_major', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rev_minor', full_name='haomo.hidelivery.hdmap.Header.rev_minor', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='haomo.hidelivery.hdmap.Header.left', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top', full_name='haomo.hidelivery.hdmap.Header.top', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='haomo.hidelivery.hdmap.Header.right', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom', full_name='haomo.hidelivery.hdmap.Header.bottom', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='haomo.hidelivery.hdmap.Header.vendor', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=312,
  serialized_end=557,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='haomo.hidelivery.hdmap.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.hidelivery.hdmap.Map.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crosswalk', full_name='haomo.hidelivery.hdmap.Map.crosswalk', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='junction', full_name='haomo.hidelivery.hdmap.Map.junction', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane', full_name='haomo.hidelivery.hdmap.Map.lane', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_sign', full_name='haomo.hidelivery.hdmap.Map.stop_sign', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signal', full_name='haomo.hidelivery.hdmap.Map.signal', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yield', full_name='haomo.hidelivery.hdmap.Map.yield', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlap', full_name='haomo.hidelivery.hdmap.Map.overlap', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_area', full_name='haomo.hidelivery.hdmap.Map.clear_area', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_bump', full_name='haomo.hidelivery.hdmap.Map.speed_bump', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road', full_name='haomo.hidelivery.hdmap.Map.road', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parking_space', full_name='haomo.hidelivery.hdmap.Map.parking_space', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pnc_junction', full_name='haomo.hidelivery.hdmap.Map.pnc_junction', index=12,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=560,
  serialized_end=1238,
)

_HEADER.fields_by_name['projection'].message_type = _PROJECTION
_MAP.fields_by_name['header'].message_type = _HEADER
_MAP.fields_by_name['crosswalk'].message_type = map__crosswalk__pb2._CROSSWALK
_MAP.fields_by_name['junction'].message_type = map__junction__pb2._JUNCTION
_MAP.fields_by_name['lane'].message_type = map__lane__pb2._LANE
_MAP.fields_by_name['stop_sign'].message_type = map__stop__sign__pb2._STOPSIGN
_MAP.fields_by_name['signal'].message_type = map__signal__pb2._SIGNAL
_MAP.fields_by_name['yield'].message_type = map__yield__sign__pb2._YIELDSIGN
_MAP.fields_by_name['overlap'].message_type = map__overlap__pb2._OVERLAP
_MAP.fields_by_name['clear_area'].message_type = map__clear__area__pb2._CLEARAREA
_MAP.fields_by_name['speed_bump'].message_type = map__speed__bump__pb2._SPEEDBUMP
_MAP.fields_by_name['road'].message_type = map__road__pb2._ROAD
_MAP.fields_by_name['parking_space'].message_type = map__parking__space__pb2._PARKINGSPACE
_MAP.fields_by_name['pnc_junction'].message_type = map__pnc__junction__pb2._PNCJUNCTION
DESCRIPTOR.message_types_by_name['Projection'] = _PROJECTION
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Map'] = _MAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTION,
  '__module__' : 'map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.hdmap.Projection)
  })
_sym_db.RegisterMessage(Projection)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.hdmap.Header)
  })
_sym_db.RegisterMessage(Header)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.hidelivery.hdmap.Map)
  })
_sym_db.RegisterMessage(Map)


# @@protoc_insertion_point(module_scope)
