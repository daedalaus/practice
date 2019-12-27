# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy.core.engine import Response
from scrapy import Request
from scrapy import signals
from scrapy.exceptions import IgnoreRequest


def mytest(*args, **kwargs):
    print('#############################  mytest ', args, kwargs)

class ScrapydownloadertestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapydownloadertestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agents = [
            'agent1',
            'agent2',
            'agent3',
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)

    def process_response(self, request, response, spider):
        response.status = 201
        return response

flag = False


class Middleware1():
    def process_request(self, request, spider):
        global flag
        with open('test.txt', 'a') as f:
            f.write('request  111\n')

        # with open('flag.txt', 'w+') as g:
        #     flag = g.read()
        #     print(flag)
        #     g.write('hello')
        # if flag:
        #     print('yes ============')
        #     return None
        # else:
        #     flag = True
        #     print('no ============')
        #     return request
        # return Response('https://httpbin.org/get')
        # return Request('http://httpbin.org/get?hello=world')

    def process_response(self, request, response, spider):
        with open('test.txt', 'a') as f:
            f.write('response  111\n')
        return response


    def process_exception(self, request, exception, spider):
        with open('test.txt', 'a') as f:
            f.write('exception  111\n')
        return


class Middleware2():
    def process_request(self, request, spider):
        with open('test.txt', 'a') as f:
            f.write('request  222\n')
        return

    def process_response(self, request, response, spider):
        with open('test.txt', 'a') as f:
            f.write('response  222\n')
        return response

    def process_exception(self, request, exception, spider):
        with open('test.txt', 'a') as f:
            f.write('exception  222\n')
        return


class Middleware3():
    def process_request(self, request, spider):
        with open('test.txt', 'a') as f:
            f.write('request  333\n')
        return

    def process_response(self, request, response, spider):
        with open('test.txt', 'a') as f:
            f.write('response  333\n')
        return response
        # raise IgnoreRequest

    def process_exception(self, request, exception, spider):
        with open('test.txt', 'a') as f:
            f.write('exception  333\n')
        return
