import requests

# url = 'http://47.103.138.66:8050/render.html?url=https://www.baidu.com'
# response = requests.get(url)
# print(response.content.decode(encoding='utf-8'))

url = 'http://47.103.138.66:8050/render.png?' \
      'url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)
