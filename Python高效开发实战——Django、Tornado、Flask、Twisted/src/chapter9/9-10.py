import datetime
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol


def long_operation(p):
    import time
    time.sleep(5)
    print('%s: The protocol %s has been started for 5 seconds.' % (datetime.datetime.now(), p))


class Echo(DatagramProtocol):
    def startProtocol(self):
        print(datetime.datetime.now(), ': started')
        reactor.callInThread(long_operation, self)


protocol = Echo()

reactor.listenUDP(8007, protocol)
reactor.run()
