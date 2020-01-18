from hashlib import md5
import re
from urllib.request import urlopen


def md5_encode(string):
    """
    MD5 encode
    """
    return md5(string.encode('utf-8')).hexdigest()


def get_referer_url(request):
    """
    get request referer url address,default /
    """
    return request.META.get('HTTP_REFERER', '/')

