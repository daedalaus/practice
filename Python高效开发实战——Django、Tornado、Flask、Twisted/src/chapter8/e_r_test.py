from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    level = Column(Integer)
    address = Column(String(50))

    class_teachers = relationship('ClassTeacher', backref='class')
    students = relationship('Student', backref='class')


class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    address = Column(String(50))
    class_id = Column(Integer, ForeignKey('class.class_id'))


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(10))
    telephone = Column(String(50))
    address = Column(String(50))
    class_teachers = relationship('ClassTeacher', backref='teacher')


class ClassTeacher(Base):
    __tablename__ = 'class_teacher'
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.class_id'), primary_key=True)


def insert_class():
    session.add(Class(class_id=1, name='三年级二班', level=3, address='李冰路410号1楼'))
    session.add(Class(class_id=2, name='五年级一班', level=5, address='李冰路410号3楼'))
    session.add(Class(class_id=3, name='五年级二班', level=5, address='李冰路410号3楼'))


def insert_student():
    session.add(Student(student_id=1, class_id=1, name='李晓', age=10, gender='男', address='虹口区...'))
    session.add(Student(student_id=2, class_id=1, name='单梦童', age=10, gender='女', address='虹口区...'))
    session.add(Student(student_id=3, class_id=1, name='林一雷', age=9, gender='女', address='闸北区...'))
    session.add(Student(student_id=4, class_id=2, name='丁辉', age=10, gender='男', address='宝山区...'))
    session.add(Student(student_id=5, class_id=2, name='王文文', age=12, gender='女', address='虹口区...'))
    session.add(Student(student_id=6, class_id=2, name='李超凡', age=11, gender='男', address='闸北区...'))
    session.add(Student(student_id=7, class_id=1, name='魏伟', age=10, gender='男', address='虹口区...'))
    session.add(Student(student_id=8, class_id=3, name='李白', age=12, gender='男', address='闸北区...'))
    session.add(Student(student_id=9, class_id=3, name='赵蕊', age=12, gender='女', address='宝山区...'))


if __name__ == '__main__':
    engine = create_engine("mysql://root:root@localhost:3306/test_database", max_overflow=5)
    DBSession = sessionmaker(engine)
    session = DBSession()
    Base.metadata.create_all(engine)
    session.commit()
    insert_class()
    insert_student()
    session.commit()
