import requests

# r = requests.get('http://httpbin.org/get')
# print(r.text)

data = {'name': 'germey', 'age': 22}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
# print(r.json())
print(type(r.json()))
