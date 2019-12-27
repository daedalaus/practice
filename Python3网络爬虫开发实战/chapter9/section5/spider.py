from urllib.parse import urlencode
import requests
from requests import Session, ReadTimeout, ConnectionError
from pyquery import PyQuery
from config import *
from db import RedisQueue
from mysql import MySQL
from request import WeixinRequest


class Spider(object):
    base_url = 'https://weixin.sogou.com/weixin'
    keyword = 'NBA'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'SMYUV=1569638989439786; CXID=BB80F44EDBC921518E678ED9AA1B911C; SUID=89DD5'
                  '6653765860A5DAAE82500089467; ad=Zlllllllll2N$mkOlllllVL$fKclllllBqbNAylll'
                  'lylllll9Cxlw@@@@@@@@@@@; ABTEST=1|1571669538|v1; IPLOC=CN3100; weixinInde'
                  'xVisited=1; SUV=006553E86556DAAC5DADC6247100B726; sct=1; SNUID=D0A72A187D'
                  '79E9C65402BE887D8C59AF; JSESSIONID=aaakI00EknVI_gItpqc4w; ppinf=5|1572007'
                  '710|1573217310|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozOjEyM3xjcn'
                  'Q6MTA6MTU3MjAwNzcxMHxyZWZuaWNrOjM6MTIzfHVzZXJpZDo0NDpvOXQybHVMX2t2aGhLbWk'
                  'xbDhQT3ExRUpwdjhRQHdlaXhpbi5zb2h1LmNvbXw; pprdig=F1ng54zSBmmXEhoI0QDLRR6l'
                  'YhXQDkCGnyJZGcD3LqdTxxuVJS9Srm6fu07Fxj2m5No-BgCjXLAgt293GTMKSCfVGk_Anvqo-'
                  'IyDKGMYVS3rr4ImSrcg7A9SkelCx4YszS8EPElcoFHrlpgkLW7iDvkrRoQ4kfd7zljxgUFM-9'
                  'I; sgid=22-38189045-AV2y7x6FPWtq7rjreOwQJkk; ppmdig=1572007711000000c5886'
                  '8545e09fc5dce78874c52510095',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like '
                      'Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
        """
        从代理池获取代理
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response and response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = PyQuery(response.text)
        items = doc('.news-list>li>.txt-box>h3>a').items()
        for item in items:
            url = item.attr('href') # 可能会出错
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next_page = doc('#sogou_next').attr('href')
        if next_page:
            url = self.base_url + str(next_page)
            weixin_request = WeixinRequest(url, callback=self.parse_index)
            yield weixin_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = PyQuery(response.text)
        data = {
            'title': doc('#activity-name').text(),
            'content': doc('#js_content').text(),
            'date': doc('#publish_time').text(),
            'nickname': doc('#js_profile_qrcode>div>strong').text(),
            'wechat': doc('#js_profile_qrcode>div>p:nth-child(1)>span').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': 'http://' + proxy,
                        'https': 'https://' + proxy
                    }
                    return self.session.send(weixin_request.prepare(),
                         timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
                return self.session.send(weixin_request.prepare(),
                         timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time += 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', result)
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        elif isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
