from twisted.internet import defer

d = defer.Deferred()  # 定义Defer实例


def print_square(n):  # 正常处理函数
    print('Square of %d is %d' % (n, n * n))
    return n


def process_error(f):  # 错误处理函数
    print('error when process')


def print_twice(n):
    print('Twice of %d is %d' % (n, 2 * n))
    return n


d.addCallback(print_square)  # 添加正常处理回调函数
d.addErrback(process_error)  # 添加错误处理回调函数
d.addCallback(print_twice)  # 添加第2个正常处理回调函数

d.callback(5)
