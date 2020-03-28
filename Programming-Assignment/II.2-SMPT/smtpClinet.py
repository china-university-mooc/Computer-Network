from socket import *

mailserver = 'smtp.163.com'
username = 'emhhbmd6aGFvbm54QDE2My5jb20='
password = 'QWJjMTk5NDExMDI='

fromMail = 'zhangzhaonnx@163.com'
toMail = '2442647554@qq.com'
subject = '2020 Organizational Structure Update'
msg = \
'''Dear TW China, 

Here's the latest org structure update from TW North America announced by Chris Murphy, MD of TW NA. 

Please feel free to contact me if you have any questions or comments. 

Pan Lei
Market Partner'''

def send(command):
    command += '\r\n'
    print("C: " + command, end='')
    clientSocket.send(command.encode())

def recv(code):
    recv = clientSocket.recv(1024).decode()
    print("S: " + recv, end='')
    if recv[:3] != code:
        raise RuntimeError('{} reply not received from server.'.format(code))

def sendAndRecv(command, code='250'):
    send(command)
    recv(code)

def sendMail():
    # HELO
    recv('220')
    sendAndRecv('HELO Alice')

    # AUTH LOGIN
    print()
    sendAndRecv('AUTH LOGIN', '334')
    sendAndRecv(username, '334')
    sendAndRecv(password, '235')

    # MAIL FROM & RCPT TO
    print()
    sendAndRecv('MAIL FROM: <{}>'.format(fromMail))
    sendAndRecv('RCPT TO: <{}>'.format(toMail))

    # DATA
    print()
    sendAndRecv('DATA', '354')
    send('From: {}'.format(fromMail))
    send('To: {}'.format(toMail))
    send('Subject: {}'.format(subject))
    for line in msg.split('\n'):
        send(line)
    sendAndRecv('.')

    # QUIT
    print()
    sendAndRecv('QUIT', '221')

def main():
    global clientSocket
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((mailserver, 25))
        sendMail()
    finally:
        clientSocket.close()

main()
