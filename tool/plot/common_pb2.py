# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='singa',
  serialized_pb='\n\x0c\x63ommon.proto\x12\x05singa\"I\n\nBlobProtos\x12\x1f\n\x05\x62lobs\x18\x01 \x03(\x0b\x32\x10.singa.BlobProto\x12\x0b\n\x03ids\x18\x02 \x03(\x05\x12\r\n\x05names\x18\x03 \x03(\t\"\x81\x01\n\x05\x44\x61tum\x12\x10\n\x08\x63hannels\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\r\n\x05label\x18\x05 \x01(\x05\x12\x12\n\nfloat_data\x18\x06 \x03(\x02\x12\x16\n\x07\x65ncoded\x18\x07 \x01(\x08:\x05\x66\x61lse\"y\n\tBlobProto\x12\x0e\n\x03num\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\x08\x63hannels\x18\x02 \x01(\x05:\x01\x30\x12\x11\n\x06height\x18\x03 \x01(\x05:\x01\x30\x12\x10\n\x05width\x18\x04 \x01(\x05:\x01\x30\x12\x10\n\x04\x64\x61ta\x18\x05 \x03(\x02\x42\x02\x10\x01\x12\x10\n\x04\x64iff\x18\x06 \x03(\x02\x42\x02\x10\x01\"8\n\x11LabelFeatureProto\x12\r\n\x05label\x18\x01 \x03(\x05\x12\t\n\x01x\x18\x02 \x03(\x02\x12\t\n\x01y\x18\x03 \x03(\x02\")\n\x07Records\x12\x1e\n\x07records\x18\x01 \x03(\x0b\x32\r.singa.Record\"\x8a\x01\n\x06Record\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32\x12.singa.Record.Type:\x11kSingleLabelImage\x12,\n\x05image\x18\x02 \x01(\x0b\x32\x1d.singa.SingleLabelImageRecord\"\x1d\n\x04Type\x12\x15\n\x11kSingleLabelImage\x10\x00\"S\n\x16SingleLabelImageRecord\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\r\n\x05label\x18\x02 \x01(\x05\x12\r\n\x05pixel\x18\x03 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x02*\xb7\x01\n\x07MsgType\x12\x08\n\x04kGet\x10\x00\x12\x08\n\x04kPut\x10\x01\x12\t\n\x05kSync\x10\x02\x12\x0b\n\x07kUpdate\x10\x03\x12\x10\n\x0ckSyncRequest\x10\x04\x12\x11\n\rkSyncResponse\x10\x05\x12\t\n\x05kStop\x10\x06\x12\t\n\x05kData\x10\x07\x12\t\n\x05kRGet\x10\x08\x12\x0c\n\x08kRUpdate\x10\t\x12\x0c\n\x08kConnect\x10\n\x12\x0b\n\x07kMetric\x10\x0b\x12\x11\n\rkSyncReminder\x10\x0c*V\n\nEntityType\x12\x10\n\x0ckWorkerParam\x10\x00\x12\x10\n\x0ckWorkerLayer\x10\x01\x12\x0b\n\x07kServer\x10\x02\x12\t\n\x05kStub\x10\x03\x12\x0c\n\x08kRuntime\x10\x04*)\n\x0bShareOption\x12\x0e\n\nkValueOnly\x10\x00\x12\n\n\x06kWhole\x10\x01*.\n\x0e\x43onnectionType\x12\r\n\tkOneToOne\x10\x00\x12\r\n\tkOneToAll\x10\x01')

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='singa.MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kGet', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kPut', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSync', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kUpdate', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSyncRequest', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSyncResponse', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStop', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kData', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRGet', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRUpdate', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kConnect', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMetric', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSyncReminder', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=681,
  serialized_end=864,
)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
_ENTITYTYPE = _descriptor.EnumDescriptor(
  name='EntityType',
  full_name='singa.EntityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kWorkerParam', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kWorkerLayer', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kServer', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStub', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRuntime', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=866,
  serialized_end=952,
)

EntityType = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPE)
_SHAREOPTION = _descriptor.EnumDescriptor(
  name='ShareOption',
  full_name='singa.ShareOption',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kValueOnly', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kWhole', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=954,
  serialized_end=995,
)

ShareOption = enum_type_wrapper.EnumTypeWrapper(_SHAREOPTION)
_CONNECTIONTYPE = _descriptor.EnumDescriptor(
  name='ConnectionType',
  full_name='singa.ConnectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kOneToOne', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kOneToAll', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=997,
  serialized_end=1043,
)

ConnectionType = enum_type_wrapper.EnumTypeWrapper(_CONNECTIONTYPE)
kGet = 0
kPut = 1
kSync = 2
kUpdate = 3
kSyncRequest = 4
kSyncResponse = 5
kStop = 6
kData = 7
kRGet = 8
kRUpdate = 9
kConnect = 10
kMetric = 11
kSyncReminder = 12
kWorkerParam = 0
kWorkerLayer = 1
kServer = 2
kStub = 3
kRuntime = 4
kValueOnly = 0
kWhole = 1
kOneToOne = 0
kOneToAll = 1


_RECORD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='singa.Record.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kSingleLabelImage', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=564,
  serialized_end=593,
)


_BLOBPROTOS = _descriptor.Descriptor(
  name='BlobProtos',
  full_name='singa.BlobProtos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blobs', full_name='singa.BlobProtos.blobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='singa.BlobProtos.ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='singa.BlobProtos.names', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=23,
  serialized_end=96,
)


_DATUM = _descriptor.Descriptor(
  name='Datum',
  full_name='singa.Datum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='singa.Datum.channels', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='singa.Datum.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='singa.Datum.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='singa.Datum.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='singa.Datum.label', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='singa.Datum.float_data', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoded', full_name='singa.Datum.encoded', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  extension_ranges=[],
  serialized_start=99,
  serialized_end=228,
)


_BLOBPROTO = _descriptor.Descriptor(
  name='BlobProto',
  full_name='singa.BlobProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='singa.BlobProto.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channels', full_name='singa.BlobProto.channels', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='singa.BlobProto.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='singa.BlobProto.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='singa.BlobProto.data', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    _descriptor.FieldDescriptor(
      name='diff', full_name='singa.BlobProto.diff', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=230,
  serialized_end=351,
)


_LABELFEATUREPROTO = _descriptor.Descriptor(
  name='LabelFeatureProto',
  full_name='singa.LabelFeatureProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='singa.LabelFeatureProto.label', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='singa.LabelFeatureProto.x', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='singa.LabelFeatureProto.y', index=2,
      number=3, type=2, cpp_type=6, label=3,
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
  extension_ranges=[],
  serialized_start=353,
  serialized_end=409,
)


_RECORDS = _descriptor.Descriptor(
  name='Records',
  full_name='singa.Records',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='singa.Records.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=411,
  serialized_end=452,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='singa.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='singa.Record.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='singa.Record.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECORD_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=455,
  serialized_end=593,
)


_SINGLELABELIMAGERECORD = _descriptor.Descriptor(
  name='SingleLabelImageRecord',
  full_name='singa.SingleLabelImageRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='singa.SingleLabelImageRecord.shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='singa.SingleLabelImageRecord.label', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pixel', full_name='singa.SingleLabelImageRecord.pixel', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='singa.SingleLabelImageRecord.data', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  extension_ranges=[],
  serialized_start=595,
  serialized_end=678,
)

_BLOBPROTOS.fields_by_name['blobs'].message_type = _BLOBPROTO
_RECORDS.fields_by_name['records'].message_type = _RECORD
_RECORD.fields_by_name['type'].enum_type = _RECORD_TYPE
_RECORD.fields_by_name['image'].message_type = _SINGLELABELIMAGERECORD
_RECORD_TYPE.containing_type = _RECORD;
DESCRIPTOR.message_types_by_name['BlobProtos'] = _BLOBPROTOS
DESCRIPTOR.message_types_by_name['Datum'] = _DATUM
DESCRIPTOR.message_types_by_name['BlobProto'] = _BLOBPROTO
DESCRIPTOR.message_types_by_name['LabelFeatureProto'] = _LABELFEATUREPROTO
DESCRIPTOR.message_types_by_name['Records'] = _RECORDS
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['SingleLabelImageRecord'] = _SINGLELABELIMAGERECORD

class BlobProtos(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLOBPROTOS

  # @@protoc_insertion_point(class_scope:singa.BlobProtos)

class Datum(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATUM

  # @@protoc_insertion_point(class_scope:singa.Datum)

class BlobProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLOBPROTO

  # @@protoc_insertion_point(class_scope:singa.BlobProto)

class LabelFeatureProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELFEATUREPROTO

  # @@protoc_insertion_point(class_scope:singa.LabelFeatureProto)

class Records(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECORDS

  # @@protoc_insertion_point(class_scope:singa.Records)

class Record(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECORD

  # @@protoc_insertion_point(class_scope:singa.Record)

class SingleLabelImageRecord(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SINGLELABELIMAGERECORD

  # @@protoc_insertion_point(class_scope:singa.SingleLabelImageRecord)


_BLOBPROTO.fields_by_name['data'].has_options = True
_BLOBPROTO.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
_BLOBPROTO.fields_by_name['diff'].has_options = True
_BLOBPROTO.fields_by_name['diff']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')
# @@protoc_insertion_point(module_scope)
