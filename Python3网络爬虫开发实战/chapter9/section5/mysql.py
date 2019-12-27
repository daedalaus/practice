import pymysql
from config import *


class MySQL(object):
    def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, username=MYSQL_USER,
                 password=MYSQL_PASSWORD, database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param port:
        :param username:
        :param password:
        :param database:
        """
        try:
            # self.db = pymysql.connect(host=host, port=port, username=username,
            #                           password=password, database=database, charset='utf8')
            self.db = pymysql.connect(host=host, port=port, user=username,
                                      password=password)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    def insert(self, table, data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into {table} values {keys} {values}'.format(
            table=table, keys=keys, values=values
        )
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()


if __name__ == '__main__':
    mysql = MySQL()
    ret = mysql.cursor.execute('SHOW DATABASES;')
    print(ret)

