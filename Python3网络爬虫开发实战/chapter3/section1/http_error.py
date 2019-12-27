def simple():
    from urllib import request, error

    url = 'http://cuiqingcai.com/index.html'

    try:
        request.urlopen(url)
    except error.HTTPError as e:
        print(e.code, e.reason, e.headers, sep='\n')


def reason_type():
    import socket
    from urllib import request, error

    url = 'http://cuiqingcai.com/index.html'

    try:
        request.urlopen(url, timeout=0.01)
    except error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')


if __name__ == '__main__':
    reason_type()