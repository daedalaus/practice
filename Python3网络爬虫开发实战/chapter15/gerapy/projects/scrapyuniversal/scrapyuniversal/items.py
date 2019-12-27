# -*- coding: utf-8 -*-

from scrapy import Item, Field


class NewsItem(Item):
    title = Field()
    url = Field()
    text = Field()
    datetime = Field()
    source = Field()
    website = Field()
