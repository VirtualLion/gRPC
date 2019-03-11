# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sat_score.proto

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
  name='sat_score.proto',
  package='satscore',
  syntax='proto3',
  serialized_pb=_b('\n\x0fsat_score.proto\x12\x08satscore\">\n\x0cRequestScore\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0e\n\x06people\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x05\"\x16\n\x05Score\x12\r\n\x05score\x18\x01 \x01(\x05\";\n\x08\x41veScore\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0e\n\x06people\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\x32\x87\x01\n\x0cSATScoreInfo\x12\x35\n\x08GetScore\x12\x16.satscore.RequestScore\x1a\x0f.satscore.Score\"\x00\x12@\n\x0c\x41verageScore\x12\x16.satscore.RequestScore\x1a\x12.satscore.AveScore\"\x00(\x01\x30\x01\x62\x06proto3')
)




_REQUESTSCORE = _descriptor.Descriptor(
  name='RequestScore',
  full_name='satscore.RequestScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='satscore.RequestScore.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='people', full_name='satscore.RequestScore.people', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='satscore.RequestScore.time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=29,
  serialized_end=91,
)


_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='satscore.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='satscore.Score.score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=115,
)


_AVESCORE = _descriptor.Descriptor(
  name='AveScore',
  full_name='satscore.AveScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='satscore.AveScore.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='people', full_name='satscore.AveScore.people', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='satscore.AveScore.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=117,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['RequestScore'] = _REQUESTSCORE
DESCRIPTOR.message_types_by_name['Score'] = _SCORE
DESCRIPTOR.message_types_by_name['AveScore'] = _AVESCORE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestScore = _reflection.GeneratedProtocolMessageType('RequestScore', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSCORE,
  __module__ = 'sat_score_pb2'
  # @@protoc_insertion_point(class_scope:satscore.RequestScore)
  ))
_sym_db.RegisterMessage(RequestScore)

Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), dict(
  DESCRIPTOR = _SCORE,
  __module__ = 'sat_score_pb2'
  # @@protoc_insertion_point(class_scope:satscore.Score)
  ))
_sym_db.RegisterMessage(Score)

AveScore = _reflection.GeneratedProtocolMessageType('AveScore', (_message.Message,), dict(
  DESCRIPTOR = _AVESCORE,
  __module__ = 'sat_score_pb2'
  # @@protoc_insertion_point(class_scope:satscore.AveScore)
  ))
_sym_db.RegisterMessage(AveScore)



_SATSCOREINFO = _descriptor.ServiceDescriptor(
  name='SATScoreInfo',
  full_name='satscore.SATScoreInfo',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=179,
  serialized_end=314,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetScore',
    full_name='satscore.SATScoreInfo.GetScore',
    index=0,
    containing_service=None,
    input_type=_REQUESTSCORE,
    output_type=_SCORE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AverageScore',
    full_name='satscore.SATScoreInfo.AverageScore',
    index=1,
    containing_service=None,
    input_type=_REQUESTSCORE,
    output_type=_AVESCORE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SATSCOREINFO)

DESCRIPTOR.services_by_name['SATScoreInfo'] = _SATSCOREINFO

# @@protoc_insertion_point(module_scope)
