import sys
from twisted.internet import defer
from twisted.python import failure

d = defer.Deferred()  # 定义Defer实例


# 以下是Defer回调函数添加阶段
def print_square(n):  # 正常处理函数
    print('Square of %d is %d' % (n, n * n))


def process_error(f):  # 错误处理函数
    print('error when process')


d.addCallback(print_square)  # 添加正常处理回调函数
d.addErrback(process_error)  # 添加错误处理回调函数


# 以下是Defer调用阶段
if len(sys.argv) > 1 and sys.argv[1] == 'call_error':
    f = failure.Failure(Exception('my exception'))
    d.errback(f)  # 调用错误处理函数process_error
else:
    d.callback(4)  # 调用正常处理函数print_square(4)
