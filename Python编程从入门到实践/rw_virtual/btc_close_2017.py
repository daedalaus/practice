from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen
import json
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
# print(file_urllib)

req2 = requests.get(json_url)
with open('data/btc_close_2017_requests.json', 'w') as g:
    g.write(req2.text)
file_requests = req2.json()
print(file_urllib == file_requests)
