# -*- coding: utf-8 -*-
import json
import time
from scrapy import Spider, Request
from weibo.items import UserItem, UserRelationItem, WeiboItem


class WeibocnSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    user_url = 'https://m.weibo.cn/profile/info?uid={uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?' \
                 'containerid=231051_-_followers_-_{uid}&page={page}'
    fan_url = 'https://m.weibo.cn/api/container/getIndex?' \
              'containerid=231051_-_fans_-_{uid}&since_id={page}'
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?containerid=' \
                '230413{uid}_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={page}'
    start_users = ['3217179555', '1742566624']

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse_user)
    
    def parse(self, response):
        pass
    
    def parse_user(self, response):
        """
        解析用户信息
        """
        result = json.loads(response.text)
        if result.get('data').get('user'):
            user_info = result.get('data').get('user')
            user_item = UserItem()
            field_map = {
                'id': 'id', 'name': 'screen_name', 'avatar': 'profile_image_url', 'cover': 'cover_image_phone',
                'gender': 'gender', 'description': 'description', 'fans_count': 'followers_count',
                'follows_count': 'follow_count', 'weibos_count': 'statuses_count', 'verified': 'verified',
                'verified_reason': 'verified_reason', 'verified_type': 'verified_type'
            }
            for field, attr in field_map.items():
                user_item[field] = user_info.get(attr)
            yield user_item

            uid = user_info.get('id')
            # 关注
            yield Request(self.follow_url.format(uid=uid, page=1), callback=self.parse_follows,
                          meta={'page': 1, 'uid': uid})
            # 粉丝
            yield Request(self.fan_url.format(uid=uid, page=1), callback=self.parse_fans,
                          meta={'page': 1, 'uid': uid})
            # 微博
            yield Request(self.weibo_url.format(uid=uid, page=1), callback=self.parse_weibos,
                          meta={'page': 1, 'uid': uid})

    def parse_follows(self, response):
        """
        解析用户关注
        :param response: Response对象
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) \
            and result.get('data').get('cards')[-1].get('card_group'):
            # 解析用户
            follows = []
            card_group = result.get('data').get('cards')[-1].get('card_group')
            for card in card_group:
                if card.get('user'):
                    uid = card.get('user').get('id')
                    name = card.get('user').get('screen_name')
                    follows.append({'id': uid, 'name': name})
                    yield Request(self.user_url.format(uid=uid), callback=self.parse_user)
            # 关注列表
            uid = response.meta.get('uid')
            user_relation_item = UserRelationItem()
            user_relation_item['id'] = uid
            user_relation_item['follows'] = follows
            user_relation_item['fans'] = []
            yield user_relation_item
            # 下一页关注
            page = response.meta.get('page')
            yield Request(self.follow_url.format(uid=uid, page=page),
                          callback=self.parse_follows, meta={'page': page, 'uid': uid})
    
    def parse_fans(self, response):
        """
        解析用户粉丝
        :param response: Response对象
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards') and len(result.get('data').get('cards')) \
                and result.get('data').get('cards')[-1].get('card_group'):
            # 解析用户
            fans = []
            card_group = result.get('data').get('cards')[-1].get('card_group')
            for card in card_group:
                uid = card.get('user').get('id')
                name = card.get('user').get('screen_name')
                fans.append({'id': uid, 'name': name})
                yield Request(self.user_url.format(uid=uid), callback=self.parse_user)
            uid = response.meta.get('uid')
            # 粉丝列表
            user_relation_item = UserRelationItem()
            user_relation_item['id'] = uid
            user_relation_item['fans'] = fans
            user_relation_item['follows'] = []
            yield user_relation_item
            # 下一页粉丝
            page = response.meta.get('page')
            yield Request(self.fan_url.format(uid=uid, page=page), callback=self.parse_fans,
                          meta={'page': page, 'uid': uid})

    def parse_weibos(self, response):
        """
        解析微博列表
        :param response: Response对象
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weibos = result.get('data').get('cards')
            for weibo in weibos:
                mblog = weibo.get('mblog')
                if mblog:
                    weibo_item = WeiboItem()
                    field_map = {
                        'id': 'id', 'attitudes_count': 'attitudes_count', 'comments_count': 'comments_count',
                        'created_at': 'created_at', 'reposts_count': 'reposts_count', 'picture': 'original_pic',
                        'pictures': 'pics', 'source': 'source', 'text': 'text', 'raw_text': 'raw_text',
                        'thumbnail': 'thumbnail_pic'
                    }
                    for field, attr in field_map.items():
                        weibo_item[field] = mblog.get(attr)
                    weibo_item['user'] = response.meta.get('uid')
                    yield weibo_item

            # 下一页微博
            uid = response.meta.get('uid')
            page = response.meta.get('page') + 1
            yield Request(self.weibo_url.format(uid=uid, page=page), callback=self.parse_weibos,
                          meta={'uid': uid, 'page': page})
