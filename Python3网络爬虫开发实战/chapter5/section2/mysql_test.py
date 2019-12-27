import pymysql


def test1():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root')
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version: ', data)
    cursor.execute('SHOW DATABASES')
    print(cursor.fetchall())
    print('---------------------')
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
    cursor.execute('SHOW DATABASES')
    print(cursor.fetchall())
    db.close()


def test2():
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         password='root', db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) ' \
          'NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


def test3():
    id = '20120001'
    user = 'Bob'
    age = 20

    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    sql = 'INSERT INTO students (id, name, age) values (%s, %s, %s)'
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()


def test4():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    table = 'students'
    data = {
        'id': '20120001',
        'name': 'Bob',
        'age': 20,
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table} ({keys}) values ({values})'.format(
        table=table, keys=keys, values=values)
    print(sql)
    try:
        cursor.execute(sql, tuple(data.values()))
        db.commit()
        print('Successful')
    except Exception as e:
        print(e)
        db.rollback()
        print('Failed')
    db.close()


def test5():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    data = {
        'id': '20120001',
        'name': 'Bob',
        'age': 21,
    }
    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(
        table=table, keys=keys, values=values
    )
    update = ','.join([' {key} = %s'.format(key=key) for key in data])
    sql += update
    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        db.commit()
        print('Successful')
    except Exception as e:
        db.rollback()
        print('Failed')
        print(e)
    finally:
        db.close()


def test6():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    table = 'students'
    condition = 'age > 20'
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
        print('Successful')
    except Exception as e:
        db.rollback()
        print('Failed')
        print(e)
    finally:
        db.close()


def test7():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    sql = 'SELECT * FROM students WHERE age >= 20'
    try:
        cursor.execute(sql)
        print(cursor.rowcount)
        one = cursor.fetchone()
        print('One: ', one)
        results = cursor.fetchall()
        print('Results: ', results)
        print('Results type: ', type(results))
        for row in results:
            print(row)
    except Exception as e:
        db.rollback()
        print('Failed')
        print(e)
    finally:
        db.close()


def test8():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders')
    cursor = db.cursor()
    sql = 'SELECT * FROM students WHERE age >= 20'
    try:
        cursor.execute(sql)
        print('Count: ', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row: ', row)
            row = cursor.fetchone()
    except Exception as e:
        db.rollback()
        print('Failed')
        print(e)
    finally:
        db.close()


if __name__ == '__main__':
    test8()

