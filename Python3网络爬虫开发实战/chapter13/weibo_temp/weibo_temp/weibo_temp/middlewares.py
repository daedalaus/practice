# -*- coding: utf-8 -*-
import logging


class CookiesMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_request(self, request, spider):
        self.logger.debug('正在设置cookies')
        request.meta['proxy'] = 'http://47.103.138.66:8050'
        # request.cookies = cookies
        # with open('cookies.txt', 'w', encoding='utf-8') as f:
        #     f.write(request.cookies)
        # with open('proxy,txt', 'w', encoding='utf-8') as f:
        #     f.write(request.meta.get('proxy'))

    @classmethod
    def from_crawler(cls, crawler):
        # settings = crawler.settings
        return cls()