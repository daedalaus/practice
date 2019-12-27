# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapyuniversal import urls
from scrapyuniversal.utils import get_config
from scrapyuniversal.rules import rules
from scrapyuniversal.items import NewsItem
from scrapyuniversal.loaders import ChinaLoader


class UniversalSpider(CrawlSpider):
    name = 'universal'
    
    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item_conf = self.config.get('item')
        if item_conf:
            item = eval(item_conf.get('class'))()
            loader = eval(item_conf.get('loader'))(item, response=response)
            # 动态获取属性配置
            for key, value in item_conf.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    elif extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args', **{'re': extractor.get('re')}))
                    elif extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    elif extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()
