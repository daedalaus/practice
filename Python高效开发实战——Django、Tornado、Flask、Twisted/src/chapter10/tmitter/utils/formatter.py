import re
from urllib.request import urlopen

from django.core.paginator import Paginator
from django.shortcuts import render_to_response

from tmitter.settings import *


def substr(content, length, add_dot=True):
    """
    字符串截取
    """
    if len(content) > length:
        content = content[:length]
    if add_dot:
        content = content[:len(content)-3] + '...'
    return content


def tiny_url(url):
    """
    将url转换成tinyurl
    """
    api_url = 'http://tinyurl.com/api-create.php?url='
    tiny_url_ = urlopen(api_url + url)
    return tiny_url_


def content_tiny_url(content):
    """
    让消息里面的连接转换成更短的Tinyurl
    """
    regex_url = r'http:\/\/([\w.]+\/?)\S*'
    for match in re.finditer(regex_url, content):
        url = match.group(0)
        content = content.replace(url, tiny_url(url))
    return content


def page_bar(objects, page_index, username='', template='control/home_pagebar.html'):
    """
    生成HTML分页控件,要使用template
    :param objects: 数据列表
    :param page_index: 当前页数
    :param username: 目前被访问的空间的用户名，没有传空
    :param template: 分页模板
    """
    page_index = int(page_index)
    _paginator = Paginator(objects, PAGE_SIZE)

    if username:
        template = 'control/user_pagebar.html'

    return render_to_response(
        template, {
            'paginator': _paginator,
            'username': username,
            'has_pages': _paginator.num_pages > 1,
            'has_next': _paginator.page(page_index).has_next(),
            'has_prev': _paginator.page(page_index).has_previous(),
            'page_index': page_index,
            'page_next': page_index + 1,
            'page_prev': page_index - 1,
            'page_count': _paginator.num_pages,
            'row_count': _paginator.count,
            'page_nums': range(_paginator.num_pages+1)[1:],
        }
    ).content.decode('utf-8')
