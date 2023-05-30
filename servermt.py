from socket import *
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def handle_request(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        if filename == '/':
            filename = '/index.html'        
        f = open(filename[1:])
        outputdata = f.read()
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + outputdata
        connectionSocket.send(response.encode())
        connectionSocket.close()
    except IOError:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(response.encode())
        connectionSocket.close()

while True:
    print('Server siap...MT')
    connectionSocket, addr = serverSocket.accept()
    t = threading.Thread(target=handle_request, args=(connectionSocket, addr))
    t.start()
