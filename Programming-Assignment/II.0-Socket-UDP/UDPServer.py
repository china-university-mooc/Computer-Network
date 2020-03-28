from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    
    message = message.decode('utf-8')
    print('receive message: ' + message)
    modifiedMessage = str(message.count('s'))

    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)

serverSocket.close()