# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_feature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_feature.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11map_feature.proto\"b\n\x0bMapsFeature\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\"\n\rlanes_feature\x18\x02 \x03(\x0b\x32\x0b.MapFeature\x12\x1c\n\tlane_info\x18\x03 \x03(\x0b\x32\t.LaneInfo\"\"\n\nLanePoints\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"\x81\x02\n\x08LaneInfo\x12$\n\x08position\x18\x01 \x01(\x0e\x32\x12.LaneInfo.Position\x12\x17\n\x0fleft_mark_index\x18\x02 \x01(\r\x12\x18\n\x10right_mark_index\x18\x03 \x01(\r\x12\x12\n\nlane_width\x18\x04 \x01(\x01\x12\n\n\x02id\x18\x05 \x01(\r\"|\n\x08Position\x12\x0c\n\x08\x45GO_LANE\x10\x00\x12\x0e\n\nRIGHT_LANE\x10\x01\x12\x16\n\x12\x42OLLARD_RIGHT_LANE\x10\x02\x12\x15\n\x11\x42OLLARD_LEFT_LANE\x10\x03\x12\r\n\tLEFT_LANE\x10\x04\x12\x14\n\x10POSITION_INVALID\x10\x63\"W\n\tPolyParas\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\x12\t\n\x01\x63\x18\x03 \x01(\x01\x12\t\n\x01\x64\x18\x04 \x01(\x01\x12\x0f\n\x07x_start\x18\x05 \x01(\x01\x12\r\n\x05x_end\x18\x06 \x01(\x01\"\xa6\x05\n\nMapFeature\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\n\n\x02id\x18\x02 \x01(\r\x12\x1a\n\x05point\x18\x03 \x03(\x0b\x32\x0b.LanePoints\x12\x1e\n\x04type\x18\x04 \x01(\x0e\x32\x10.MapFeature.Type\x12&\n\x08position\x18\x05 \x01(\x0e\x32\x14.MapFeature.Position\x12\x1c\n\x08geometry\x18\x06 \x01(\x0b\x32\n.PolyParas\"\xa6\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rSINGLE_DASHED\x10\x01\x12\x11\n\rDOUBLE_DASHED\x10\x02\x12\x10\n\x0c\x44OUBLE_SOLID\x10\x03\x12\x10\n\x0cSINGLE_SOLID\x10\x04\x12\x1b\n\x17RIGHT_SOLID_LEFT_DASHED\x10\x05\x12\x1b\n\x17LEFT_SOLID_RIGHT_DASHED\x10\x06\x12\r\n\tROAD_EDGE\x10\x07\"\xcd\x02\n\x08Position\x12\x0c\n\x08MID_LINE\x10\x00\x12\r\n\tHOST_LEFT\x10\x01\x12\x0e\n\nHOST_RIGHT\x10\x02\x12\r\n\tNEXT_LEFT\x10\x03\x12\x0e\n\nNEXT_RIGHT\x10\x04\x12\x0e\n\nNNEXT_LEFT\x10\x05\x12\x0f\n\x0bNNEXT_RIGHT\x10\x06\x12\x18\n\x14HOST_LEFT_SUBSIDIARY\x10\x07\x12\x19\n\x15HOST_RIGHT_SUBSIDIARY\x10\x08\x12\x18\n\x14NEXT_LEFT_SUBSIDIARY\x10\t\x12\x19\n\x15NEXT_RIGHT_SUBSIDIARY\x10\n\x12\x19\n\x15NNEXT_LEFT_SUBSIDIARY\x10\x0b\x12\x1a\n\x16NNEXT_RIGHT_SUBSIDIARY\x10\x0c\x12\r\n\tCURB_LEFT\x10\r\x12\x0e\n\nCURB_RIGHT\x10\x0e\x12\x14\n\x10POSITION_INVALID\x10\x63\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LANEINFO_POSITION = _descriptor.EnumDescriptor(
  name='Position',
  full_name='LaneInfo.Position',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EGO_LANE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_LANE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOLLARD_RIGHT_LANE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOLLARD_LEFT_LANE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_LANE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITION_INVALID', index=5, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=291,
  serialized_end=415,
)
_sym_db.RegisterEnumDescriptor(_LANEINFO_POSITION)

_MAPFEATURE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='MapFeature.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_DASHED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_DASHED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_SOLID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_SOLID', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_SOLID_LEFT_DASHED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_SOLID_RIGHT_DASHED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROAD_EDGE', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=683,
  serialized_end=849,
)
_sym_db.RegisterEnumDescriptor(_MAPFEATURE_TYPE)

_MAPFEATURE_POSITION = _descriptor.EnumDescriptor(
  name='Position',
  full_name='MapFeature.Position',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MID_LINE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_LEFT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_RIGHT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_LEFT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_RIGHT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NNEXT_LEFT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NNEXT_RIGHT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_LEFT_SUBSIDIARY', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_RIGHT_SUBSIDIARY', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_LEFT_SUBSIDIARY', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEXT_RIGHT_SUBSIDIARY', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NNEXT_LEFT_SUBSIDIARY', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NNEXT_RIGHT_SUBSIDIARY', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURB_LEFT', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURB_RIGHT', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITION_INVALID', index=15, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=852,
  serialized_end=1185,
)
_sym_db.RegisterEnumDescriptor(_MAPFEATURE_POSITION)


_MAPSFEATURE = _descriptor.Descriptor(
  name='MapsFeature',
  full_name='MapsFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MapsFeature.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lanes_feature', full_name='MapsFeature.lanes_feature', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_info', full_name='MapsFeature.lane_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=119,
)


_LANEPOINTS = _descriptor.Descriptor(
  name='LanePoints',
  full_name='LanePoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='LanePoints.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='LanePoints.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=155,
)


_LANEINFO = _descriptor.Descriptor(
  name='LaneInfo',
  full_name='LaneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='LaneInfo.position', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_mark_index', full_name='LaneInfo.left_mark_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_mark_index', full_name='LaneInfo.right_mark_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_width', full_name='LaneInfo.lane_width', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='LaneInfo.id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LANEINFO_POSITION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=415,
)


_POLYPARAS = _descriptor.Descriptor(
  name='PolyParas',
  full_name='PolyParas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='PolyParas.a', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='PolyParas.b', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='c', full_name='PolyParas.c', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='d', full_name='PolyParas.d', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_start', full_name='PolyParas.x_start', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_end', full_name='PolyParas.x_end', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=504,
)


_MAPFEATURE = _descriptor.Descriptor(
  name='MapFeature',
  full_name='MapFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MapFeature.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='MapFeature.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='MapFeature.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='MapFeature.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='MapFeature.position', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='MapFeature.geometry', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MAPFEATURE_TYPE,
    _MAPFEATURE_POSITION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=1185,
)

_MAPSFEATURE.fields_by_name['lanes_feature'].message_type = _MAPFEATURE
_MAPSFEATURE.fields_by_name['lane_info'].message_type = _LANEINFO
_LANEINFO.fields_by_name['position'].enum_type = _LANEINFO_POSITION
_LANEINFO_POSITION.containing_type = _LANEINFO
_MAPFEATURE.fields_by_name['point'].message_type = _LANEPOINTS
_MAPFEATURE.fields_by_name['type'].enum_type = _MAPFEATURE_TYPE
_MAPFEATURE.fields_by_name['position'].enum_type = _MAPFEATURE_POSITION
_MAPFEATURE.fields_by_name['geometry'].message_type = _POLYPARAS
_MAPFEATURE_TYPE.containing_type = _MAPFEATURE
_MAPFEATURE_POSITION.containing_type = _MAPFEATURE
DESCRIPTOR.message_types_by_name['MapsFeature'] = _MAPSFEATURE
DESCRIPTOR.message_types_by_name['LanePoints'] = _LANEPOINTS
DESCRIPTOR.message_types_by_name['LaneInfo'] = _LANEINFO
DESCRIPTOR.message_types_by_name['PolyParas'] = _POLYPARAS
DESCRIPTOR.message_types_by_name['MapFeature'] = _MAPFEATURE

MapsFeature = _reflection.GeneratedProtocolMessageType('MapsFeature', (_message.Message,), dict(
  DESCRIPTOR = _MAPSFEATURE,
  __module__ = 'map_feature_pb2'
  # @@protoc_insertion_point(class_scope:MapsFeature)
  ))
_sym_db.RegisterMessage(MapsFeature)

LanePoints = _reflection.GeneratedProtocolMessageType('LanePoints', (_message.Message,), dict(
  DESCRIPTOR = _LANEPOINTS,
  __module__ = 'map_feature_pb2'
  # @@protoc_insertion_point(class_scope:LanePoints)
  ))
_sym_db.RegisterMessage(LanePoints)

LaneInfo = _reflection.GeneratedProtocolMessageType('LaneInfo', (_message.Message,), dict(
  DESCRIPTOR = _LANEINFO,
  __module__ = 'map_feature_pb2'
  # @@protoc_insertion_point(class_scope:LaneInfo)
  ))
_sym_db.RegisterMessage(LaneInfo)

PolyParas = _reflection.GeneratedProtocolMessageType('PolyParas', (_message.Message,), dict(
  DESCRIPTOR = _POLYPARAS,
  __module__ = 'map_feature_pb2'
  # @@protoc_insertion_point(class_scope:PolyParas)
  ))
_sym_db.RegisterMessage(PolyParas)

MapFeature = _reflection.GeneratedProtocolMessageType('MapFeature', (_message.Message,), dict(
  DESCRIPTOR = _MAPFEATURE,
  __module__ = 'map_feature_pb2'
  # @@protoc_insertion_point(class_scope:MapFeature)
  ))
_sym_db.RegisterMessage(MapFeature)


# @@protoc_insertion_point(module_scope)
