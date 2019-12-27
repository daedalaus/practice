from requests import Request, Session

url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

s = Session()
req = Request('POST',url, headers, data=data)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
