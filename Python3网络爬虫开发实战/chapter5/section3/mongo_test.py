import pymongo


def test1():
    # client = pymongo.MongoClient(host='localhost', port=27017)
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # db = client.test
    db = client['test']

    # collection = db.students
    collection = db['students']


def test2():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male',
    }
    result = collection.insert(student)
    print(result)


def test3():
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male',
    }
    student2 = {
        'id': '20170102',
        'name': 'Mike',
        'age': 21,
        'gender': 'male',
    }
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    result = collection.insert([student1, student2])
    print(result)


def test4():
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male',
    }
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    result = collection.insert_one(student)
    print(result)
    print(result.inserted_id)


def test5():
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male',
    }
    student2 = {
        'id': '20170102',
        'name': 'Mike',
        'age': 21,
        'gender': 'male',
    }
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    result = collection.insert_many((student1, student2))
    print(result)
    print(result.inserted_ids)


def test6():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    result = collection.find_one({'name': 'Mike'})
    print(type(result))
    print(result)


def test7():
    from bson.objectid import ObjectId
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    result = collection.find_one({'_id': ObjectId('5d9469ab35f6ae1084847acb')})
    print(result)


def test8():
    # client = pymongo.Mongoclient(host='localhost', )
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    # results = collection.find({'age': 20})
    # results = collection.find({'age': {'$gt': 20}})
    results = collection.find({'name': {'$regex': '^M.*'}})
    print(type(results))
    print(results)
    for result in results:
        print(result)


def test9():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    # count = collection.find().count()
    count = collection.find({'age': 20}).count()
    print(count)


def test10():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    # results = collection.find().sort('name', pymongo.ASCENDING)
    results = collection.find().sort('name', pymongo.DESCENDING)
    for result in results:
        print(result)


def test11():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    # results = collection.find().sort('name', pymongo.DESCENDING).skip(2).limit(3)
    from bson.objectid import ObjectId
    results = collection.find({'_id': {'$gt': ObjectId('5d946a3835f6ae2bb88c1c17')}})
    for result in results:
        print(result)


def test12():
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    condition = {'name': 'Mike'}
    student = collection.find_one(condition)
    student['name'] = 'Kevin'
    result = collection.update(condition, student)
    print(result)


def test13():
    from bson.objectid import ObjectId
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    student = {'name': 'Tom'}
    # condition = {'name': 'Jordan'}
    condition = {'_id': ObjectId('5d9466bc35f6ae0e748538b0')}
    result = collection.update(condition, student)
    print(result)


def test14():
    from bson.objectid import ObjectId
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.test
    collection = db.students
    condition = {'_id': ObjectId('5d9469b735f6ae27bc25fcf1')}
    student = {'city': 'Shanghai', 'loc': 'wanguo'}
    result = collection.update(condition, {'$set': student})
    print(result)


def test15():
    from bson.objectid import ObjectId
    client = pymongo.MongoClient(host='localhost', port=27017)
    # db = client.test
    # collection = db.students
    collection = client.test.students
    condition = {'_id': ObjectId('5d9469ab35f6ae1084847acb')}
    student = {'age': 26}
    result = collection.update_one(condition, {'$set': student})
    print(type(result))
    print(result)
    print(result.matched_count)
    print(result.modified_count)


def test16():
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client.test.students
    condition = {'gender': 'male'}
    results = collection.update_many(condition, {'$inc': {'age': 50}})
    print(type(results))
    print(results)
    print(results.matched_count)
    print(results.modified_count)


def test17():
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client.test.students
    result = collection.remove({'name': 'Kevin'})
    print(result)


def test18():
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client.test.students
    result = collection.delete_one({'name': 'Jordan'})
    print(type(result))
    print(result)
    print(result.deleted_count)


def test19():
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client.test.students
    results = collection.delete_many({'name': 'Jordan'})
    print(type(results))
    print(results)
    print(results.deleted_count)


if __name__ == '__main__':
    test19()
