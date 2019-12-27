import time
from io import BytesIO

from PIL import Image
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from chaojiying import ChaoJiYingClient
from jiyan import CrackGeetest

EMAIL = 'test@test.com'
PASSWORD = '123456'
# 超级鹰用户名、密码、软件ID、验证码类型
CHAOJIYING_USERNAME = '18638235241'
CHAOJIYING_PASSWORD = 'lzy6885300'
CHAOJIYING_SOFT_ID = 901856
CHAOJIYING_KIND = 9004


class JiYanClick(object):
    def __init__(self, browser, wait):
        self.url = 'https://login.flyme.cn/sso'
        # self.browser = Chrome()
        # self.wait = WebDriverWait(self.browser, 20)
        self.browser = browser
        self.wait = wait
        self.email = EMAIL
        self.chaojiying = ChaoJiYingClient(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD,
                                           CHAOJIYING_SOFT_ID)

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        username_el = self.wait.until(EC.presence_of_element_located((By.ID, 'account')))
        password_el = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        username_el.clear()
        username_el.send_keys(EMAIL)
        password_el.clear()
        password_el.send_keys(PASSWORD)
        button_el = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_btn')))
        button_el.click()
        time.sleep(2)
        # Chrome().find_element_by_class_name('geetest_btn').text
        print('button text is: ', button_el.text)
        if button_el.text == '验证成功':
            self.open()

    def get_click_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_btn')))
        return button

    def get_click_element(self):
        """
        获取验证图像
        :return: 图片对象
        """
        # element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_item_img')))
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_item_wrap')))
        return element

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元素
        """
        element = self.get_click_element()
        time.sleep(2)
        location = element.location
        size = element.size
        rangle = location['x'], location['y'], location['x'] + \
                                   size['width'], location['y'] + size['height']
        return [int(loc * 1.25) for loc in rangle]
        # return rangle

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        self.browser.save_screenshot('screen.png')
        screenshot = self.browser.get_screenshot_as_png()
        # screenshot = Image.open('screen.png')
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_click_image(self, name='captcha.png'):
        """
        获取验证码图片
        :param name: 图片对象
        """
        left, top, right, bottom = self.get_position()
        print('验证码位置', left, top, right, bottom)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def get_click_order(self):
        image = self.get_click_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        # raise Exception('暂时跳过识别')
        # 识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        pic_id = result.get('pic_id')
        self.chaojiying.pic_id = pic_id
        return result

    def get_points(self, captcha_result):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(int(number)/1.25) for number in group.split(',')] for group in groups]
        # locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        """
        点击验证图片
        :param locations: 点击位置
        :return: None
        """
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_click_element(),
                   location[0], location[1]).click().perform()
            time.sleep(1)

    def validate(self):
        # self.browser = Chrome()
        ack_el = self.browser.find_element_by_class_name('geetest_commit')
        ack_el.click()
        # button = self.browser.find_element_by_class_name('geetest_radar_tip')
        # button = self.browser.find_element_by_class_name('geetest_success_radar_tip')
        flag = self.wait.until(EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, '.geetest_success_radar_tip_content'), '验证成功'))
        # attr = button.get_attribute('aria-label')
        print(flag)
        attr = self.browser.find_element_by_class_name('geetest_success_radar_tip_content').text
        if attr == '验证成功':
            print('attr: ', attr)
            print('实验成功')
        else:
            print(attr)
            print('超级鹰识别失败')
            print('button text: ', attr)
            # self.chaojiying.report_error(self.chaojiying.pic_id)

    def main(self):
        # self.open()
        result = self.get_click_order()
        locations = self.get_points(result)
        self.touch_click_words(locations)
        self.validate()


class Control(object):
    def __init__(self):
        self.url = 'https://login.flyme.cn/sso'
        self.browser = Chrome()
        # self.browser.fullscreen_window()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.jiyan = CrackGeetest(self.browser, self.wait)
        self.click = JiYanClick(self.browser, self.wait)

    def get_crack_category(self):
        try:
            self.click.get_click_element()
            return 'click'
        except TimeoutException as e:
            # self.click.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
            return 'slide'

    def main(self):
        self.click.open()
        cate = self.get_crack_category()
        if cate == 'click':
            self.click.main()
        else:
            self.jiyan.main()


if __name__ == '__main__':
    ct = Control()
    ct.main()
