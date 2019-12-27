from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Spider(object):
    def __init__(self, timeout):
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.browser.set_page_load_timeout(self.timeout)
        self.browser.get('https://login.taobao.com/member/login.jhtml')
        try:
            login_trans = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.quick-form .login-links>a:nth-child(1)')))
            login_trans.click()
        except TimeoutException:
            pass
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
        submit_el = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@class="J_Submit"]')
        ))
        submit_el.click()

        while True:
            try:
                cmd = input('hehe')
                eval(cmd)
            except Exception as e:
                print(e.args)

        # self.browser.set_window_size(1400, 700)
        # self.browser.set_page_load_timeout(self.timeout)

    def get(self, url):
        self.browser.get(url)


if __name__ == '__main__':
    sp = Spider(10)
    sp.get('https://s.taobao.com/search?q=iPad')