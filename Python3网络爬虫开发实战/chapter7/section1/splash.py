# import requests
# from urllib.parse import quote

lua = '''
function main(splash)
  return 'hello'
end
'''

lua2 = '''
function main(splash)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html=treat.as_string(response.body),
            url=response.url,
            status=response.status
        }
end
'''

# url = 'http://cloud:8050/execute?lua_source=' + quote(lua2)
# response = requests.get(url)
# print(response.text)

# response = requests.get('http://cloud:8044')
# print(response.status_code)

import requests
from urllib.parse import quote
import re

lua3 = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return treat.as_string(response.body)
end
'''

url = 'http://cloud:8050/execute?lua_source=' + quote(lua3)
response = requests.get(url, auth=('admin', 'admin'))
ip = re.search(r'(\d+\.\d+\.\d+\.\d+)', response.text).group(1)
print(ip)
