# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relative_map.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import pnc_point_pb2 as pnc__point__pb2
import map_pb2 as map__pb2
import perception_pb2 as perception__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='relative_map.proto',
  package='haomo.relative_map',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x12relative_map.proto\x12\x12haomo.relative_map\x1a\x0cheader.proto\x1a\x0fpnc_point.proto\x1a\tmap.proto\x1a\x10perception.proto\"V\n\x0eNavigationPath\x12-\n\x04path\x18\x01 \x01(\x0b\x32\x1f.haomo.hidelivery.planning.Path\x12\x15\n\rpath_priority\x18\x02 \x01(\r\"q\n\x0eNavigationInfo\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12;\n\x0fnavigation_path\x18\x02 \x03(\x0b\x32\".haomo.relative_map.NavigationPath\"\xb2\x02\n\x06MapMsg\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.haomo.hios.Header\x12*\n\x05hdmap\x18\x02 \x01(\x0b\x32\x1b.haomo.hidelivery.hdmap.Map\x12G\n\x0fnavigation_path\x18\x03 \x03(\x0b\x32..haomo.relative_map.MapMsg.NavigationPathEntry\x12\x34\n\troad_info\x18\x04 \x01(\x0b\x32!.haomo.hidelivery.perception.Road\x1aY\n\x13NavigationPathEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".haomo.relative_map.NavigationPath:\x02\x38\x01'
  ,
  dependencies=[header__pb2.DESCRIPTOR,pnc__point__pb2.DESCRIPTOR,map__pb2.DESCRIPTOR,perception__pb2.DESCRIPTOR,])




_NAVIGATIONPATH = _descriptor.Descriptor(
  name='NavigationPath',
  full_name='haomo.relative_map.NavigationPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='haomo.relative_map.NavigationPath.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path_priority', full_name='haomo.relative_map.NavigationPath.path_priority', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=188,
)


_NAVIGATIONINFO = _descriptor.Descriptor(
  name='NavigationInfo',
  full_name='haomo.relative_map.NavigationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.relative_map.NavigationInfo.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_path', full_name='haomo.relative_map.NavigationInfo.navigation_path', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=303,
)


_MAPMSG_NAVIGATIONPATHENTRY = _descriptor.Descriptor(
  name='NavigationPathEntry',
  full_name='haomo.relative_map.MapMsg.NavigationPathEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='haomo.relative_map.MapMsg.NavigationPathEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='haomo.relative_map.MapMsg.NavigationPathEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=612,
)

_MAPMSG = _descriptor.Descriptor(
  name='MapMsg',
  full_name='haomo.relative_map.MapMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='haomo.relative_map.MapMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hdmap', full_name='haomo.relative_map.MapMsg.hdmap', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='navigation_path', full_name='haomo.relative_map.MapMsg.navigation_path', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_info', full_name='haomo.relative_map.MapMsg.road_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAPMSG_NAVIGATIONPATHENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=612,
)

_NAVIGATIONPATH.fields_by_name['path'].message_type = pnc__point__pb2._PATH
_NAVIGATIONINFO.fields_by_name['header'].message_type = header__pb2._HEADER
_NAVIGATIONINFO.fields_by_name['navigation_path'].message_type = _NAVIGATIONPATH
_MAPMSG_NAVIGATIONPATHENTRY.fields_by_name['value'].message_type = _NAVIGATIONPATH
_MAPMSG_NAVIGATIONPATHENTRY.containing_type = _MAPMSG
_MAPMSG.fields_by_name['header'].message_type = header__pb2._HEADER
_MAPMSG.fields_by_name['hdmap'].message_type = map__pb2._MAP
_MAPMSG.fields_by_name['navigation_path'].message_type = _MAPMSG_NAVIGATIONPATHENTRY
_MAPMSG.fields_by_name['road_info'].message_type = perception__pb2._ROAD
DESCRIPTOR.message_types_by_name['NavigationPath'] = _NAVIGATIONPATH
DESCRIPTOR.message_types_by_name['NavigationInfo'] = _NAVIGATIONINFO
DESCRIPTOR.message_types_by_name['MapMsg'] = _MAPMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NavigationPath = _reflection.GeneratedProtocolMessageType('NavigationPath', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONPATH,
  '__module__' : 'relative_map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.relative_map.NavigationPath)
  })
_sym_db.RegisterMessage(NavigationPath)

NavigationInfo = _reflection.GeneratedProtocolMessageType('NavigationInfo', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONINFO,
  '__module__' : 'relative_map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.relative_map.NavigationInfo)
  })
_sym_db.RegisterMessage(NavigationInfo)

MapMsg = _reflection.GeneratedProtocolMessageType('MapMsg', (_message.Message,), {

  'NavigationPathEntry' : _reflection.GeneratedProtocolMessageType('NavigationPathEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPMSG_NAVIGATIONPATHENTRY,
    '__module__' : 'relative_map_pb2'
    # @@protoc_insertion_point(class_scope:haomo.relative_map.MapMsg.NavigationPathEntry)
    })
  ,
  'DESCRIPTOR' : _MAPMSG,
  '__module__' : 'relative_map_pb2'
  # @@protoc_insertion_point(class_scope:haomo.relative_map.MapMsg)
  })
_sym_db.RegisterMessage(MapMsg)
_sym_db.RegisterMessage(MapMsg.NavigationPathEntry)


_MAPMSG_NAVIGATIONPATHENTRY._options = None
# @@protoc_insertion_point(module_scope)