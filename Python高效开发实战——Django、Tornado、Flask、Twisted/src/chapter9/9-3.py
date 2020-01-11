from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import threading
import time
import datetime

host = '127.0.0.1'
port = 8007


class Echo(DatagramProtocol):  # 定义DatagramProtocol子类
    def datagramReceived(self, datagram, addr):
        print('Got data from: %s: %s' % (addr, datagram.decode('utf-8')))


protocol = Echo()  # 实例化Protocol子类


def routine():
    time.sleep(1)  # 确保protocol已经启动
    while True:
        protocol.transport.write(('%s: say hello to myself.' % datetime.datetime.now()).encode('utf-8'),
                                 (host, port))
        time.sleep(5)  # 每隔5秒向服务器发送消息


threading.Thread(target=routine).start()
reactor.listenUDP(port, protocol)
reactor.run()  # 挂起运行
