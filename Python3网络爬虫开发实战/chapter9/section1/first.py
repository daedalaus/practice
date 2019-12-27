from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener


url = 'http://httpbin.org/get'
proxy = '47.103.138.66:8050'
# proxy = 'feiyu:123456@47.103.138.66:8050'
# 正向代理nginx配置中不能设置auth_basic "Please input password"
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
})
opener = build_opener(proxy_handler)

try:
    # response = urlopen(url)
    response = opener.open(url)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)


'''
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "101.86.221.137, 101.86.221.137", 
  "url": "https://httpbin.org/get"
}
'''

'''
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "47.103.138.66, 47.103.138.66", 
  "url": "https://httpbin.org/get"
}
'''