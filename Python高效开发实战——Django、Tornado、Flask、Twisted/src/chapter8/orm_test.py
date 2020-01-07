from contextlib import contextmanager
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
# import orm

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    title = Column(String(50))
    salary = Column(Integer)

    def is_active(self):
        # 假设所有用户都是活跃用户
        return True

    def get_id(self):
        # 返回账号ID，用方法返回属性值提高了表的封装性
        return self.id

    def is_authenticated(self):
        # 假设已经通过验证
        return True

    def is_anonymous(self):
        # 具有登录名和密码的账号不是匿名用户
        return False


db_connect_string = 'mysql://root:root@localhost:3306/test_database?charset=utf8'
# ssl_args = {}
engine = create_engine(db_connect_string)
session_type = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))


def get_session():
    return session_type()


@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def InsertAccount(user, password, title, salary):
    with session_scope() as session:
        account = Account(user_name=user, password=password, title=title, salary=salary)
        session.add(account)


def GetAccount(id=None, user_name=None):
    with session_scope() as session:
        return session.query(Account).filter(or_(Account.id==id, Account.user_name==user_name)).first()


def DeleteAccount(user_name):
    with session_scope() as session:
        account = GetAccount(user_name=user_name)
        if account:
            session.delete(account)


def UpdateAccount(id, user_name, password, title, salary):
    with session_scope() as session:
        account = session.query(Account).filter(Account.id==id).first()
        if not account: return
        account.user_name = user_name
        account.password = password
        account.title = title
        account.salary = salary


InsertAccount('David Li', '123', 'System Manager', 3000)
InsertAccount('Rebeca Li', '', 'Accountant', 3000)

account = GetAccount(2)

DeleteAccount('Howard')

UpdateAccount(1, 'admin', 'none', 'System Admin', 2000)
