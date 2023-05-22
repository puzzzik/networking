from base64 import b64encode

import grpc
from app.models import File as ModelsFile
from .file_service_pb2 import File, MetaData, DownloadRequest, FileListRequest, GetFileRequest, RemoveFileRequest
from .file_service_pb2_grpc import GreeterStub



class Client:
    def __init__(self):
        self.host = 'localhost:50051'

    def download_file(self, bucket_name: str, file_name: str):
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            file = stub.DownloadFile(
                DownloadRequest(bucket=bucket_name, filename=file_name)
            )
            return file

    def upload_file(self, file: ModelsFile, data) -> MetaData:
        with data.open('rb+') as f:
            with grpc.insecure_channel(self.host) as channel:
                stub = GreeterStub(channel)
                return stub.UploadFile(
                    File(
                        chunk_data=f.read(),
                        bucket=file.get_bucket_name(),
                        filename=str(file.name),
                        last_modified=file.last_modified,
                    )
                )

    def remove_file(self, file_name: str, bucket_name: str):
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            stub.RemoveFile(
                RemoveFileRequest(
                    bucket=bucket_name,
                    filename=file_name
                )
            )

    def get_file_info(self, bucket_name: str, file_name: str) -> MetaData:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            meta_data = stub.GetFile(
                GetFileRequest(filename=file_name, bucket=bucket_name))
            return meta_data

    def get_file_list(self, bucket_name: str) -> list[MetaData]:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            file_list: list[MetaData] = stub.GetFileList(
                FileListRequest(
                    bucket=bucket_name
                )
            ).files
            return file_list
