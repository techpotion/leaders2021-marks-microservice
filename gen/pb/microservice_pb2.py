# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: microservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='microservice.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12microservice.proto\x12\x02pb\"\xbd\x01\n\x05Marks\x1a\x96\x01\n\nGetRequest\x12\x1a\n\x12\x61reasSquarePer100k\x18\x01 \x01(\x01\x12\x1a\n\x12\x61reasAmountPer100k\x18\x02 \x01(\x01\x12\x1b\n\x13sportsAmountPer100k\x18\x03 \x01(\x01\x12\x16\n\x0esubwayDistance\x18\x04 \x01(\x01\x12\x1b\n\x13pollutionPercentage\x18\x05 \x01(\x01\x1a\x1b\n\x0bGetResponse\x12\x0c\n\x04mark\x18\x01 \x01(\x01\x32H\n\x0cMicroservice\x12\x38\n\x07GetMark\x12\x14.pb.Marks.GetRequest\x1a\x15.pb.Marks.GetResponse\"\x00\x62\x06proto3'
)




_MARKS_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='pb.Marks.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='areasSquarePer100k', full_name='pb.Marks.GetRequest.areasSquarePer100k', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areasAmountPer100k', full_name='pb.Marks.GetRequest.areasAmountPer100k', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsAmountPer100k', full_name='pb.Marks.GetRequest.sportsAmountPer100k', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subwayDistance', full_name='pb.Marks.GetRequest.subwayDistance', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pollutionPercentage', full_name='pb.Marks.GetRequest.pollutionPercentage', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=37,
  serialized_end=187,
)

_MARKS_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='pb.Marks.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mark', full_name='pb.Marks.GetResponse.mark', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=189,
  serialized_end=216,
)

_MARKS = _descriptor.Descriptor(
  name='Marks',
  full_name='pb.Marks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_MARKS_GETREQUEST, _MARKS_GETRESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=216,
)

_MARKS_GETREQUEST.containing_type = _MARKS
_MARKS_GETRESPONSE.containing_type = _MARKS
DESCRIPTOR.message_types_by_name['Marks'] = _MARKS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Marks = _reflection.GeneratedProtocolMessageType('Marks', (_message.Message,), {

  'GetRequest' : _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
    'DESCRIPTOR' : _MARKS_GETREQUEST,
    '__module__' : 'microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.Marks.GetRequest)
    })
  ,

  'GetResponse' : _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
    'DESCRIPTOR' : _MARKS_GETRESPONSE,
    '__module__' : 'microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.Marks.GetResponse)
    })
  ,
  'DESCRIPTOR' : _MARKS,
  '__module__' : 'microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Marks)
  })
_sym_db.RegisterMessage(Marks)
_sym_db.RegisterMessage(Marks.GetRequest)
_sym_db.RegisterMessage(Marks.GetResponse)



_MICROSERVICE = _descriptor.ServiceDescriptor(
  name='Microservice',
  full_name='pb.Microservice',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=218,
  serialized_end=290,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMark',
    full_name='pb.Microservice.GetMark',
    index=0,
    containing_service=None,
    input_type=_MARKS_GETREQUEST,
    output_type=_MARKS_GETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MICROSERVICE)

DESCRIPTOR.services_by_name['Microservice'] = _MICROSERVICE

# @@protoc_insertion_point(module_scope)
