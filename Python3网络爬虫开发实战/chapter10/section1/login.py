import requests
from lxml import etree
from pyquery import PyQuery


class Login(object):
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like '
                          'Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]
        return token

    def login(self):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': 'RainingHeart',
            'password': 'lzy6885300',
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        with open('github.html', 'w', encoding='utf-8') as f:
            f.write(html)
        selector = etree.HTML(html)
        # dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        # for item in dynamics:
        #     dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
        #     print(dynamic)
        # text = selector.xpath('//div[contains(@class, "news")]/div[2]/h2/text()')
        text = selector.xpath('//div[contains(@class, "news")]/text()')
        print('text is -->', text)

        doc = PyQuery(html)
        news = doc('div.news')
        print('html-->', news.text(), '<--')

    def profile(self, html):
        selector = etree.HTML(html)
        try:
            name = selector.xpath('//input[@id="user_profile_name"]/@name')[0]
            print('name is ', name)
        except Exception as e:
            print('name ==', e.args)

        try:
            # email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
            email = selector.xpath('//select[@id="user_profile_email"]/option[1]/text()')
            print('email is ', email)
        except Exception as e:
            print('email ==', e.args)

        try:
            avatar = selector.xpath('//div[@class="avatar-upload"]//summary/img/@src')[0]
            print('avatar is ', avatar)
        except Exception as e:
            print('avatar ==', e.args)
        with open('avatar.png', 'wb') as f:
            f.write(requests.get(avatar).content)
        # print(name, email)


if __name__ == '__main__':
    login = Login()
    login.login()
