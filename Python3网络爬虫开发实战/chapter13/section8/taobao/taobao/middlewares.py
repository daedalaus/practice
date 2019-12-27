# -*- coding: utf-8 -*-
import json
import time
from logging import getLogger
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):
    def __init__(self, timeout=None, service_args=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # if service_args is None:
        #     service_args = []
        # self.browser = webdriver.PhantomJS(service_args=service_args)

        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.browser.get('https://login.taobao.com/member/login.jhtml')
        login_trans = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.quick-form .login-links>a::nth-child(1)')))
        login_trans.click()
        user_el = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@name="TPL_username"]')
        ))
        password_el = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@name="TPL_password"]')
        ))
        user_el.clear()
        user_el.send_keys('18638235241')
        password_el.clear()
        password_el.send_keys('lzy6885300')

        # self.browser.delete_all_cookies()
        # time.sleep(1)
        #
        # with open('taobao/cookies-11-9.json') as f:
        #     cookie_list = json.load(f)
        # for cookie in cookie_list:
        #     if cookie.get('expiry', None):
        #         cookie['expiry'] = int(cookie['expiry'])
        #     self.browser.add_cookie(cookie)

        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug('PhantomJS is Starting')
        page = request.meta.get('page', 1)
        try:
            self.browser.get(request.url)

            if page > 1:
                input_el = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form>input'))
                )
                submit_el = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form>span.btn.J_Submit'))
                )
                input_el.clear()
                input_el.send_keys(page)
                submit_el.click()
            self.wait.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#mainsrp-pager li.item.active>span'), str(page)))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request,
                                encoding='utf-8', status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))

