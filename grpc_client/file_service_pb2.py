# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66ile_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"S\n\x04\x46ile\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12\x15\n\rlast_modified\x18\x04 \x01(\t\"3\n\x0f\x44ownloadRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"?\n\x10\x44ownloadResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\x12\x17\n\x04meta\x18\x02 \x01(\x0b\x32\t.MetaData\"5\n\x11RemoveFileRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"\x14\n\x12RemoveFileResponse\"_\n\x08MetaData\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\x15\n\rlast_modified\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x02\"!\n\x0f\x46ileListRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\",\n\x10\x46ileListResponse\x12\x18\n\x05\x66iles\x18\x01 \x03(\x0b\x32\t.MetaData\"2\n\x0eGetFileRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t2\xfa\x01\n\x07Greeter\x12 \n\nUploadFile\x12\x05.File\x1a\t.MetaData\"\x00\x12\x35\n\x0c\x44ownloadFile\x12\x10.DownloadRequest\x1a\x11.DownloadResponse\"\x00\x12\x37\n\nRemoveFile\x12\x12.RemoveFileRequest\x1a\x13.RemoveFileResponse\"\x00\x12\x34\n\x0bGetFileList\x12\x10.FileListRequest\x1a\x11.FileListResponse\"\x00\x12\'\n\x07GetFile\x12\x0f.GetFileRequest\x1a\t.MetaData\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILE._serialized_start=55
  _FILE._serialized_end=138
  _DOWNLOADREQUEST._serialized_start=140
  _DOWNLOADREQUEST._serialized_end=191
  _DOWNLOADRESPONSE._serialized_start=193
  _DOWNLOADRESPONSE._serialized_end=256
  _REMOVEFILEREQUEST._serialized_start=258
  _REMOVEFILEREQUEST._serialized_end=311
  _REMOVEFILERESPONSE._serialized_start=313
  _REMOVEFILERESPONSE._serialized_end=333
  _METADATA._serialized_start=335
  _METADATA._serialized_end=430
  _FILELISTREQUEST._serialized_start=432
  _FILELISTREQUEST._serialized_end=465
  _FILELISTRESPONSE._serialized_start=467
  _FILELISTRESPONSE._serialized_end=511
  _GETFILEREQUEST._serialized_start=513
  _GETFILEREQUEST._serialized_end=563
  _GREETER._serialized_start=566
  _GREETER._serialized_end=816
# @@protoc_insertion_point(module_scope)