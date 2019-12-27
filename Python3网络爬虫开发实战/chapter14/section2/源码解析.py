# from scrapy_redis.queue import Base

from redis import StrictRedis, Redis
import win32process



r = StrictRedis(password='foobared')
pipe = r.pipeline()
pipe.multi()

while True:
    flag = input('输入：')
    if flag == 'yes':

        ret = pipe.zremrangebyrank('db', 0, 0)
        print(ret)
        ret2 = pipe.execute()
        print(type(ret2))
        print(ret2)
    elif flag == 'no':
        break

