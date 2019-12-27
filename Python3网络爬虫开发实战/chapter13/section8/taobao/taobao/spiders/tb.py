# -*- coding: utf-8 -*-
from urllib.parse import quote
import json
import time
from scrapy import Spider, Request

from taobao.items import ProductItem


class TbSpider(Spider):
    name = 'tb'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def parse(self, response):
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]'
        )
        items_dict = []
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class, "shop")]//text()').extract()).strip()
            item['image'] = ''.join(product.xpath(
                './/div[contains(@class, "pic")]//img[contains(@class,"img")]/@data-src').extract()).strip()
            item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()

            item_dict = {
                'price': product.xpath('.//div[contains(@class, "price")]//text()').extract(),
                'title': product.xpath('.//div[contains(@class, "title")]//text()').extract(),
                'shop': product.xpath('.//div[contains(@class, "shop")]//text()').extract(),
                'image': product.xpath(
                    './/div[contains(@class, "pic")]//img[contains(@class,"img")]/@data-src').extract()
            }
            items_dict.append(item_dict)
            yield item

        with open(str(time.time()) + '.json', 'w', encoding='utf-8') as f:
            json.dump(items_dict, f, indent=2, ensure_ascii=False)

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)
