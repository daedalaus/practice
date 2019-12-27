from redis import StrictRedis

redis = StrictRedis(password='foobared')


def test1():
    ret = redis.lrem('mylist', -2, 3)
    print(ret)


def test2():
    ret = redis.lpop('mylist')
    print(ret)


def test3():
    mem = redis.lrange('mylist', 0, -1)
    print(mem)
    redis.brpoplpush('mylist', 'mylist')
    mem = redis.lrange('mylist', 0, -1)
    print(mem)


if __name__ == '__main__':
    test3()
