# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

from scrapy import Spider, Request

from images360.items import ImageItem


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def __init__(self, *args, **kwargs):
        super(ImagesSpider, self).__init__(*args, **kwargs)
        self.logger.debug('======= spider init ===========')

    def start_requests(self):
        data = {'ch': 'photography', 'listtype': 'new'}
        base_url = 'https://images.so.com/zj?'
        for page in range(self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 10
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['image_id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
