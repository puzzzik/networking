import logging
import grpc
import file_service_pb2
from file_service_pb2_grpc import GreeterStub
from app.models import File


class Client:
    def __init__(self):
        self.host = 'localhost:50051'

    def download_file(self, bucket_name: str, file_name: str):
        pass

    def upload_file(self, bucket_name: str, file: File, chunk_data):
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            stub.UploadFile(
                file_service_pb2.File(
                    chunk_data=chunk_data,
                    meta=file_service_pb2.MetaData(
                        filename=file.name,
                        extension=file.extension,
                        bucket=file.folder.name
                    )
                )
            )

    def get_file_info(self, bucket_name: str, file_name: str) -> file_service_pb2.MetaData:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            pass

    def get_file_list(self, bucket_name: str) -> [file_service_pb2.MetaData]:
        with grpc.insecure_channel(self.host) as channel:
            stub = GreeterStub(channel)
            file_list: [file_service_pb2.MetaData] = stub.GetFileList(bucket_name=bucket_name)
            return file_list


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GreeterStub(channel)
        # download = stub.DownloadFile(
        #     file_service_pb2.MetaData(
        #         bucket='test',
        #         filename='code',
        #         extension='txt'
        #     )
        # )
        # print("Greeter client received: " + response.message)
        # with open('download_response1.txt', 'wb') as f:
        #     f.write(download.chunk_data)

        # with open('test.txt', 'rb') as f:
        #     upload = stub.UploadFile(
        #         file_service_pb2.File(
        #             chunk_data=f.read(),
        #             meta=file_service_pb2.MetaData(
        #                 filename='test',
        #                 extension='txt',
        #                 bucket='test'
        #             )
        #         )
        #     )
        # print(upload)

        # rm = stub.RemoveFile(
        #     file_service_pb2.MetaData(
        #         bucket='test',
        #         filename='test',
        #         extension='txt'
        #     )
        # )
        # print(rm)

        files = stub.GetFileList(
            file_service_pb2.FileListRequest(
                bucket='test'
            )
        )
        print(files.files)


if __name__ == '__main__':
    logging.basicConfig()
    run()
