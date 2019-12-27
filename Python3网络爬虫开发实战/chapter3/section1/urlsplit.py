from urllib.parse import urlsplit

url = 'http://www.baidu.com/index.html;user?id=5#comment'

result = urlsplit(url)
print(result)
