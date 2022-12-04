from server import MinioServer


if __name__ == '__main__':
    server = MinioServer()
    resp = server.upload_file('test.txt')
