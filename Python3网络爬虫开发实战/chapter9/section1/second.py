import socks
import socket
from urllib import request
from urllib.error import URLError


# 未实际搭建SOCKS5代理，有时间学习SOCKS5代理
socks.set_default_proxy(socks.SOCKS5, '47.103.138.66', 8050)
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
