import json
from utils import get_page
from pyquery import PyQuery


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            proxies.append(proxy)
            print('成功获取到代理', proxy)
        return proxies

    def crawl_daili66(self, page_count=15):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('66 Crawling', url)
            html = get_page(url)
            if html:
                doc = PyQuery(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    # port = tr.find('td:eq(2)').text()   ?
                    print('66 -->', ':'.join([ip, port]), '<--')
                    yield ':'.join([ip, port])

    def not_crewl_proxy360(self):
        """
        获取Proxy360
        :return: 代理
        """
        start_url = 'http://www.proxy360.cn/Region/China'
        print('360 Crawling', start_url)
        html = get_page(start_url)
        if html:
            doc = PyQuery(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                print('360 -->', td.text().replace(' ', ''), '<--')
                yield td.text().replace(' ', '')

    def crawl_goubanjia(self):
        """
        获取Goubanjia
        :return: 代理
        """
        # start_url = 'http://www.goubanjia.com/free/gngn/index.shtml'
        start_url = 'http://www.goubanjia.com'
        print('goubanjia Crawling', start_url)
        html = get_page(start_url)
        if html:
            doc = PyQuery(html)
            trs = doc('.table tbody tr').items()
            for tr in trs:
                if tr.find('td:nth-child(2)').text() == '高匿':
                    tr.find('p').remove()
                    print('goubanjia -->', tr.find('td:nth-child(1)').text().replace('\n', ''), '<--')
                    yield tr.find('td:nth-child(1)').text().replace('\n', '')
