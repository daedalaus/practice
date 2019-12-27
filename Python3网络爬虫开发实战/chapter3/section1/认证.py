from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener

url = 'http://127.0.0.1:5000'
username = 'john'
password = 'hello'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)

auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

response = opener.open(url)
print(response.read().decode())
