from twisted.internet import defer, reactor


def print_square(n):
    print('Square of %d is %d' % (n, n*n))
    return n


def print_twice(n):
    print('Twice of %d is %d' % (n, 2*n))
    return n


def make_defer():
    d = defer.Deferred()
    d.addCallback(print_square)
    d.addCallback(print_twice)
    reactor.callLater(2, d.callback, 5)


make_defer()
reactor.run()
