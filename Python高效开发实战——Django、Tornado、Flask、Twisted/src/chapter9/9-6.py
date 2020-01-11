from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

multicast_ip = '224.0.0.1'  # 组播地址
port = 8001  # 端口


class Multicast(DatagramProtocol):  # 继承自DatagramProtocol
    def startProtocol(self):
        self.transport.joinGroup(multicast_ip)  # 加入组播组
        self.transport.write(b'Notify', (multicast_ip, port))  # 组播数据

    def datagramReceived(self, datagram, addr):
        print('Datagram %s received from %s' % (repr(datagram), repr(addr)))
        if datagram == b'Notify':
            self.transport.write(b'Acknowledge', (multicast_ip, port))  # 单播回应


reactor.listenMulticast(port, Multicast(), listenMultiple=True)  # 组播监听
reactor.run()  # 挂起运行
