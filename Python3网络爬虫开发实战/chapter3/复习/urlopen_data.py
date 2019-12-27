# # # # # from urllib.request import urlopen
# # # # # from urllib.parse import urlencode
# # # # #
# # # # # dic = {
# # # # #     'name': 'lisi',
# # # # #     'age': 18
# # # # # }
# # # # # data = bytes(urlencode(dic), encoding='utf-8')
# # # # # url = 'http://httpbin.org/post'
# # # # #
# # # # # response = urlopen(url, data=data)
# # # # #
# # # # # print(response.status)
# # # # # # print(response.read().decode())
# # # # # print(response.fileno())
# # # # # print(response.msg)
# # # # # print(response.version)
# # # # # print(response.reason)
# # # # # print(response.debuglevel)
# # # # # print(response.closed)
# # # # #
# # # #
# # # # from urllib.request import Request, urlopen
# # # # from urllib.parse import urlencode
# # # #
# # # # url = 'http://httpbin.org/post'
# # # # data = bytes(urlencode({'name': 'wangwu', 'city': 'Shanghai'}), encoding='utf-8')
# # # # headers = {
# # # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
# # # #                   'Chrome/77.0.3865.90 Safari/537.36',
# # # #     'Host': 'httpbin.org'
# # # # }
# # # # req = Request(url, data=data, headers=headers, method='Post')
# # # # response = urlopen(req)
# # # # print(response.status)
# # # # print(response.read().decode())
# # # #
# # #
# # # from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# # #
# # # url = 'http://localhost:5000'
# # # p = HTTPPasswordMgrWithDefaultRealm()
# # # p.add_password(None, url, 'john', 'hello')
# # #
# # # handler = HTTPBasicAuthHandler(p)
# # # opener = build_opener(handler)
# # #
# # # r = opener.open(url)
# # # print(r.status)
# # # print(r.read().decode())
# #
# # from urllib.request import ProxyHandler, build_opener
# # from urllib.error import URLError
# #
# # url = 'http://httpbin.org/get'
# # proxies = {
# #     'http': 'http://127.0.0.1:8888',
# #     'https': 'http://127.0.0.1:9743'
# # }
# #
# # proxy_handler = ProxyHandler(proxies=proxies)
# # opener = build_opener(proxy_handler)
# # r = opener.open(url)
# # print(r.status)
# # print(r.read().decode())
# #
#
# from http.cookiejar import CookieJar, MozillaCookieJar, LWPCookieJar
# from urllib.request import HTTPCookieProcessor, build_opener
#
# url = 'https://www.baidu.com'
# # cookie = CookieJar()
# cookie = MozillaCookieJar('mozila.txt')
#
# handler = HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# r = opener.open(url)
# # for item in cookie:
# #     print(item.name, ' = ', item.value)
# cookie.save(ignore_discard=True, ignore_expires=True)
#

