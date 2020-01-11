from twisted.internet.protocol import DatagramProtocol
import socket
from twisted.internet import reactor
import threading
import time


class Echo(DatagramProtocol):
    def datagramReceived(self, datagram, addr):  # 定义DatagramProtocol子类
        print(datagram.decode('utf-8'))


def send(sock):
    while True:
        sock.sendto('Hello my friend!'.encode('utf-8'), address)
        time.sleep(1)


address = ('127.0.0.1', 8008)

recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recvSocket.setblocking(False)  # 设为阻塞模式
recvSocket.bind(address)  # 为普通socket绑定地址
port = reactor.adoptDatagramPort(recvSocket.fileno(), socket.AF_INET, Echo())  # 适配
recvSocket.close()  # 关闭普通socket

# 新建一个socket作为发送端
sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


threading.Thread(target=send, args=(sendSocket,)).start()
reactor.run()
