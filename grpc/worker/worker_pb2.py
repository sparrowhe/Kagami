# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: worker.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "worker.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cworker.proto\x12\rkagami_worker"\x1b\n\x0bSyncRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"/\n\x0cSyncResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t"$\n\x10RegisterResponse\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x01 \x01(\x08"\x1e\n\x0bRegisterAck\x12\x0f\n\x07message\x18\x01 \x01(\t2\xa7\x01\n\x06Worker\x12M\n\x12sync_from_upstream\x12\x1a.kagami_worker.SyncRequest\x1a\x1b.kagami_worker.SyncResponse\x12N\n\x0f\x61\x63\x63\x65pt_register\x12\x1f.kagami_worker.RegisterResponse\x1a\x1a.kagami_worker.RegisterAckb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "worker_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_SYNCREQUEST"]._serialized_start = 31
    _globals["_SYNCREQUEST"]._serialized_end = 58
    _globals["_SYNCRESPONSE"]._serialized_start = 60
    _globals["_SYNCRESPONSE"]._serialized_end = 107
    _globals["_REGISTERRESPONSE"]._serialized_start = 109
    _globals["_REGISTERRESPONSE"]._serialized_end = 145
    _globals["_REGISTERACK"]._serialized_start = 147
    _globals["_REGISTERACK"]._serialized_end = 177
    _globals["_WORKER"]._serialized_start = 180
    _globals["_WORKER"]._serialized_end = 347
# @@protoc_insertion_point(module_scope)