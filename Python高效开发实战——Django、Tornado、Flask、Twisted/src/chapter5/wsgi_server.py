# 引入Python的WSGI包
from wsgiref.simple_server import make_server
# 引入服务器端程序的代码
from webapp import application

# 实例化一个监听8080端口的服务器
server = make_server('127.0.0.1', 8080, application)
# 开始监听HTTP请求
server.serve_forever()
