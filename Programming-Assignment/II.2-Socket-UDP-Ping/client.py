from socket import *
import time

serverHost = 'localhost'
serverPort = 12000
ttl = 1
rounds = 10
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(ttl)
clientSocket.connect((serverHost, serverPort))

mi = 1000
ma = 0
sum = 0
loss = 0
for i in range (1, rounds + 1):
    sendTime = time.time()
    message = 'Ping {} {:.3f}'.format(i, sendTime)
    try:
        start = time.perf_counter()
        clientSocket.send(message.encode())
        response = clientSocket.recv(1024)
        rtt = (time.time() - sendTime) / 1000
        mi = min(mi, rtt)
        ma = max(ma, rtt)
        sum += rtt
        avg = sum / i
        print('Reply from {}: seq={} rtt={:.3f}ms min={:.3f}ms max={:.3f}ms avg={:.3f}ms'.format(serverHost, i, rtt, mi, ma, avg))
    except timeout:
        loss += 1
        print('Reply from {}: seq={} timeout'.format(serverHost, i))
percent = loss / rounds
print('{} packets transmitted, {} packets received, {:.1%} packet loss'.format(rounds, rounds - loss, percent))
clientSocket.close()
