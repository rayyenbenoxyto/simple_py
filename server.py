from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind(('localhost', 80))
serverSocket.listen(1)

while True:
    print('Server siap...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        print(filename)
        if filename == '/':
            filename = '/index.html'
        f = open(filename[1:])
        outputdata = f.read()
        f.close()


        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())


        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()
    except IOError:

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())


        connectionSocket.close()

serverSocket.close()
