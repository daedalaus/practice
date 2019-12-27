def simple():
    from http.cookiejar import CookieJar
    import urllib.request

    url = 'http://www.baidu.com'

    cookie = CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    response = opener.open(url)
    for item in cookie:
        print(item.name+'='+item.value)


def mozilla():
    from http.cookiejar import MozillaCookieJar
    import urllib.request

    url = 'http://www.baidu.com'
    filename = 'data/cookies.txt'
    cookie = MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)


def lwp():
    from http.cookiejar import LWPCookieJar
    import urllib.request

    url = 'http://www.baidu.com'
    filename = 'data/lwp.txt'
    cookie = LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)


def load():
    from http.cookiejar import LWPCookieJar
    import urllib.request

    url = 'http://www.baidu.com'
    filename = 'data/lwp.txt'

    cookie = LWPCookieJar()
    cookie.load(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    print(response.read().decode())


if __name__ == '__main__':
    load()
