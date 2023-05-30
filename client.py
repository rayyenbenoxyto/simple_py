import sys
from socket import *

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))

request = 'GET /%s HTTP/1.1\r\nHost: %s:%s\r\n\r\n' % (filename, serverHost, serverPort)
clientSocket.send(request.encode())

response = clientSocket.recv(1024).decode()
print(response)
clientSocket.close()
