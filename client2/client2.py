from server2 import MinioServer as serv2


if __name__ == '__main__':
    serv2 = serv2()
    resp = serv2.upload_file('test.txt')
