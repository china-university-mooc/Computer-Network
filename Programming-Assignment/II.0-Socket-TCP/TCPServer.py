from socket import *
import threading


class WordThread(threading.Thread):
    def __init__(self, conSocket):
        super().__init__()
        self.conSocket = conSocket

    def run(self):
        conSocket = self.conSocket
        message = conSocket.recv(2048)

        message = message.decode('utf-8')
        print('receive message: ' + message)
        modifiedMessage = message.upper()

        conSocket.send(modifiedMessage.encode('utf-8'))
        conSocket.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    conSocket, addr = serverSocket.accept()
    thread = WordThread(conSocket)
    thread.start()

serverSocket.close()
