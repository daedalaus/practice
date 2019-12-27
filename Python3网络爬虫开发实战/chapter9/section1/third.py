import requests


proxy = '47.103.138.66:8050'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
proxy1 = '47.103.138.66:8050'
proxies1 = {
    'http': 'socks5://' + proxy1,
    'https': 'socks5://' + proxy1
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies1)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
