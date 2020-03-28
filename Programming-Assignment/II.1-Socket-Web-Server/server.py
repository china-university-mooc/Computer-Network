from socket import *
from threading import *

class WorkThread(Thread):
    def __init__(self, conSocket):
        super().__init__()
        self.conSocket = conSocket

    def sendHeader(self, code, len=0):
        conSocket = self.conSocket
        header = 'Http/1.1 {} {}\nConnection:close\nContent-Type:text/html\nContent-Length: {}\n\n'
        des = 'OK' if code == 200 else 'Not Found'

        header = header.format(code, des, len)
        print(header.split('\n')[0])
        conSocket.send(header.encode())

    def run(self):
        conSocket = self.conSocket
        try:         
            message = conSocket.recv(1024).decode()
            print(message.split('\n')[0])
            filename = message.split()[1][1:]             
            with open(filename) as f:
                content = f.read()

            self.sendHeader(200, len(content))
            conSocket.send(content.encode())
        except IOError:
            self.sendHeader(404)
        finally:
            conSocket.close()

serverPort = 80

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)

    while True:     
        print('Ready to serve...')

        conSocket, addr = serverSocket.accept()
        thread = WorkThread(conSocket)
        thread.start()      
    serverSocket.close()

main()