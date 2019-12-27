from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode())
except URLError as e:
    print(e.reason)
