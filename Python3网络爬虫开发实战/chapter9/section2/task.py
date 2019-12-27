import socket
import requests

PROXY_POOL_URL = 'http://127.0.0.1:5000/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


proxy = get_proxy()
print('proxy get success', proxy)
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies= proxies, timeout=5)
    print(response.text)
except (requests.exceptions.ConnectionError, socket.timeout,
        requests.exceptions.ReadTimeout) as e:
    print('Error', e.args)
