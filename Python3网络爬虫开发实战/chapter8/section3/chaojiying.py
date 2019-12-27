import requests
from hashlib import md5


class ChaoJiYingClient(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = soft_id
        self.pic_id = None
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def post_pic(self, im, codetype):
        """
        :param im: 图片字节
        :param codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params, files=files, headers=self.headers)
        return r.json()

    def report_error(self, im_id):
        """
        :param im_id: 报错题目的图片ID
        """
        params = {'id': im_id}
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php',
                          data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    CHAOJIYING_USERNAME = '18638235241'
    CHAOJIYING_PASSWORD = 'lzy6885300'
    CHAOJIYING_SOFT_ID = 901856
    CHAOJIYING_KIND = 9004
    clien = ChaoJiYingClient(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
    im_id = '2083122423174500015'
    clien.report_error(im_id)
