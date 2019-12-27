from urllib import request, error
import urllib.request


try:
    response = urllib.request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)
