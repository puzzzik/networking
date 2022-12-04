from server1 import MinioServer as serv1
if __name__ == '__main__':
    server = serv1()
    resp = server.upload_file('test.txt')
