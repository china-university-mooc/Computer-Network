from socket import *

serverName = 'localhost'
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    message = input('Input lowercase sentence:')
    if (message == 'q'):
        clientSocket.close()
        break

    clientSocket.send(message.encode('utf-8'))
    modifiedMessage = clientSocket.recv(2048)

    print('From server: ' + modifiedMessage.decode('utf-8'))

    clientSocket.close()
