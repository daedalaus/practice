from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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


if __name__ == '__main__':
    engine = create_engine("mysql://root:root@localhost:3306/test_database", max_overflow=5)
    DBSession = sessionmaker(engine)
    session = DBSession()
    Base.metadata.create_all(engine)
    session.commit()
