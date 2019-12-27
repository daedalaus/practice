import time
from io import BytesIO

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PIL import Image

EMAIL = 'test@test.com'
PASSWORD = '123456'


class CrackGeetest():
    def __init__(self):
        # self.url = 'https://account.geetest.com/login'
        self.url = 'https://login.flyme.cn/sso'
        self.browser = Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_btn')))
        return button

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        with open('screen.png', 'wb') as f:
            f.write(screenshot)
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], \
                                   location['x'], location['x'] + size['width']
        return top, bottom, left, right

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :param name:
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        with open(name, 'wb') as f:
            f.write(captcha)
        return captcha

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        for i in range(3):
            if abs(pixel1[i] - pixel2[i]) >= threshold:
                return False
        else:
            return True

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = 4 / 5 * distance
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度 v = v0 + at
            v = v0 + a * t
            # 移动速度 x = v0t + 1/2 * a * t^2
            move = v0 * t + 0.5 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(move)
        return track

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param track: 滑块
        :return: 轨迹
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()


if __name__ == '__main__':
    cr = CrackGeetest()
    cr.browser.get(cr.url)
    # user_el, password_el = cr.browser.find_elements(By.CSS_SELECTOR, 'body .ivu-input')
    user_el = cr.browser.find_element_by_id('account')
    password_el = cr.browser.find_element_by_id('password')
    user_el.clear()
    user_el.send_keys(cr.email)
    password_el.clear()
    password_el.send_keys(cr.password)
    button = cr.get_geetest_button()
    button.click()
    cr.get_position()
    cr.get_geetest_image()

