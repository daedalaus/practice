from redis import StrictRedis


redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')


def test1():
    ret = redis.set('name', 'Bob')
    print(ret)
    ret = redis.get('name')
    print(ret)


def test2():
    name = redis.exists('name')
    print(name)
    age = redis.exists('age')
    print(age)


def test3():
    name = redis.delete('name')
    print(name)


def test4():
    name = redis.set('name', 'Mike')
    type_ = redis.type('name')
    print(type_)


def test5():
    keys = redis.keys('*')
    print(keys)
    keys2 = redis.keys('n*')
    print(keys2)


def test6():
    for i in range(10):
        random = redis.randomkey()
        print(random)


def test7():
    name = redis.rename('name', 'new_name')
    print(name)


def test8():
    size = redis.dbsize()
    print(size)


def test9():
    redis.set('test', 'hello')
    expire = redis.expire('test', 5)
    print(expire)


def test10():
    ttl = redis.ttl('new_name')
    print(ttl)
    ttl2 = redis.ttl('test')
    print(ttl2)
    redis.set('five', 5, ex=5)
    ttl3 = redis.ttl('five')
    print(ttl3)


def test11():
    d1 = redis.get('new_name')
    print(d1)
    mv = redis.move('new_name', 5)
    print(mv)
    d1 = redis.get('new_name')
    print(d1)


def test12():
    keys = redis.keys('*')
    print(keys)
    ret = redis.flushdb()
    print(ret)
    keys = redis.keys('*')
    print(keys)


def test13():
    ret = redis.flushall()
    print(ret)


if __name__ == '__main__':
    test13()
