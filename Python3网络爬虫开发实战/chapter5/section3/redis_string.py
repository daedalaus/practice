from redis import StrictRedis

redis = StrictRedis(host='localhost', db=0, password='foobared')


def test1():
    name = redis.set('name', 'Bob')
    print(name)


def test2():
    name = redis.get('name')
    print(name)


def test3():
    name = redis.getset('name', 'Jordan')
    print(name)


def test4():
    names = redis.mget(['name', 'nickname'])
    print(names)


def test5():
    name = redis.setnx('name', 'hello')
    print(name)
    age = redis.setnx('age', 18)
    print(age)


def test6():
    redis.setex('name', 5, 'he')


if __name__ == '__main__':
    test5()
