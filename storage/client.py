from server import MinioServer as Storage

if __name__ == '__main__':
    server = MinioServer()
    resp = server.upload_file('test.txt')
    server.download_file('test.txt')


# удаленное хранилище с gRPC
class gRPC_Service:
    def getFile(self, username: str, file_name: str):
        storage = Storage()
        try:
            file = storage.download_file(file_name)
        except:
            return Exception
        return file


# Бэк
def download_file_from_server():
    file = gRPC_Service().getFile()
    return Response(file)