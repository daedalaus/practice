# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # allowed_domains = ['m.weibo.cn']
    # start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_1936710392']

    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        with open('response.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
            f.write('\n\n')
            f.write('================================================')
        pass
