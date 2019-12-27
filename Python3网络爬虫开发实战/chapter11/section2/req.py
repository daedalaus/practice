import requests

data = {
    'name': 'zhangsan',
    'age': '18'
}

requests.post('http://127.0.0.1:5000', data=data)
