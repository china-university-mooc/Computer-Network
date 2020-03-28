from socket import *
import sys

def recv (clientSocket):
    message = bytes()
    while True:
        data = clientSocket.recv(1024)    
        if not data: 
            break
        message += data
    return message

serverName = sys.argv[1]
serverPort = eval(sys.argv[2])
fileName = sys.argv[3]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = 'GET /{} HTTP/1.1\nHost:{}\n\n'.format(fileName, serverName)
clientSocket.send(request.encode())
response = recv(clientSocket)
response = response.decode()

code = response.split()[1]
if code == '200':
    print(response.split('\n\n')[1])
else:
    print('Not Found')
