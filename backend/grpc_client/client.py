import logging
import grpc
import file_service_pb2
from file_service_pb2_grpc import GreeterStub
from app.models import File


class Client:
    def __init__(self):
        self.host = 'localhost:50051'

    def download_file(self, bucket_name: str, file_name: str):
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            file = stub.DownloadFile(file_name=file_name, bucket_name=bucket_name)
            return file

    def upload_file(self, bucket_name: str, file: File, chunk_data):
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            stub.UploadFile(
                file_service_pb2.File(
                    chunk_data=chunk_data,
                    meta=file_service_pb2.MetaData(
                        filename=file.name,
                        extension=file.extension,
                        bucket=bucket_name
                    )
                )
            )

    def get_file_info(self, bucket_name: str, file_name: str) -> file_service_pb2.MetaData:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            meta_data = stub.GetFile(file_name=file_name, bucket_name=bucket_name)
            return meta_data

    def get_file_list(self, bucket_name: str) -> [file_service_pb2.MetaData]:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            file_list: [file_service_pb2.MetaData] = stub.GetFileList(bucket_name=bucket_name)
            return file_list

