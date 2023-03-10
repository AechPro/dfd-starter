# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_server_interface.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63lient_server_interface.proto\x1a\x1cgoogle/protobuf/struct.proto\"1\n\x06\x43onfig\x12\'\n\x06params\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xd3\x01\n\x0bServerState\x12\x18\n\x10strategy_history\x18\x01 \x03(\x02\x12\x17\n\x0fstrategy_frames\x18\x02 \x03(\x02\x12\x19\n\x11policy_parameters\x18\x03 \x03(\x02\x12\x1e\n\x16strategy_history_shape\x18\x04 \x03(\x05\x12\x1d\n\x15strategy_frames_shape\x18\x05 \x03(\x05\x12\r\n\x05\x65poch\x18\x06 \x01(\x03\x12\x15\n\rexperiment_id\x18\x07 \x01(\t\x12\x11\n\tobs_stats\x18\x08 \x03(\x02\"\xe1\x01\n\x06Return\x12\r\n\x05\x65poch\x18\x01 \x01(\x03\x12\x15\n\rencoded_noise\x18\x02 \x01(\t\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12\x0f\n\x07novelty\x18\x04 \x01(\x02\x12\x0f\n\x07\x65ntropy\x18\x05 \x01(\x02\x12\x11\n\ttimesteps\x18\x06 \x01(\x05\x12\x0f\n\x07is_eval\x18\x07 \x01(\x08\x12\x13\n\x0b\x65val_states\x18\x08 \x03(\x02\x12\x19\n\x11\x65val_states_shape\x18\t \x03(\x05\x12\x18\n\x10obs_stats_update\x18\n \x03(\x02\x12\x11\n\tworker_id\x18\x0b \x01(\t\"$\n\x0bReturnArray\x12\x15\n\x04rets\x18\x01 \x03(\x0b\x32\x07.Return\"@\n\x18ServerStateQueryResponse\x12\r\n\x05\x65poch\x18\x01 \x01(\x03\x12\x15\n\rexperiment_id\x18\x02 \x01(\t\"\x06\n\x04Null2\xd7\x01\n\x0b\x43SInterface\x12\x1d\n\tGetConfig\x12\x05.Null\x1a\x07.Config\"\x00\x12\'\n\x0eGetServerState\x12\x05.Null\x1a\x0c.ServerState\"\x00\x12 \n\x0cSubmitReturn\x12\x07.Return\x1a\x05.Null\"\x00\x12&\n\rSubmitReturns\x12\x0c.ReturnArray\x1a\x05.Null\"\x00\x12\x36\n\x10QueryServerState\x12\x05.Null\x1a\x19.ServerStateQueryResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_server_interface_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIG._serialized_start=63
  _CONFIG._serialized_end=112
  _SERVERSTATE._serialized_start=115
  _SERVERSTATE._serialized_end=326
  _RETURN._serialized_start=329
  _RETURN._serialized_end=554
  _RETURNARRAY._serialized_start=556
  _RETURNARRAY._serialized_end=592
  _SERVERSTATEQUERYRESPONSE._serialized_start=594
  _SERVERSTATEQUERYRESPONSE._serialized_end=658
  _NULL._serialized_start=660
  _NULL._serialized_end=666
  _CSINTERFACE._serialized_start=669
  _CSINTERFACE._serialized_end=884
# @@protoc_insertion_point(module_scope)
