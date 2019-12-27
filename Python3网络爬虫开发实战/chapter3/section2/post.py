import requests

data = {'name': 'zhangsan', 'age': 22}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)


