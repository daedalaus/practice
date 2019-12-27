from urllib.parse import urlparse

url1 = 'http://www.baidu.com/index.html;user?id=5#comment'
result1 = urlparse(url1)
# print(type(result1), result)

url2 = 'www.baidu.com/index.html;user?id=5#comment'
result2 = urlparse(url2, scheme='https')
# print(result2)

url3 = url1
result3 = urlparse(url3, scheme='https')
print(result3)

url4 = url1
result4 = urlparse(url4, allow_fragments=False)
print(result4)

url5 = 'http://www.baidu.com/index.html#comment'
result5 = urlparse(url5, allow_fragments=False)
print(result5)
print(result5.scheme, result5[0], result5.netloc, result5[1], sep='\n')
