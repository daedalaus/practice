from pickle import dumps, loads
from redis import StrictRedis

from request import WeixinRequest

REDIS_HOST = '47.103.138.66'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
REDIS_KEY = ''


class RedisQueue(object):
    def __init__(self):
        """
        初始化 Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :return: 添加结果
        """
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, request)
        return False

    def pop(self):
        """
        取出一个Request并反序列化
        :return: Request or None
        """
        if self.db.llen(REDIS_KEY):
            return self.db.lpop(REDIS_KEY)
        else:
            return None

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0
