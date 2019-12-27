import json
from flask import Flask, g

app = Flask(__name__)
# 生成模块的配置字典
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}


@app.route('/')
def index():
    return '<h2>Welcome to Cookie Pool System</h2>'


def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('RedisClient("cookies", "' + website + '")'))
    return g


@app.route('/<website>/random')
def random(website):
    """
    获取随机的Cookie，访问地址如/weibo/random
    :param website: 随机Cookie
    :return:
    """
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies
