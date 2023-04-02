from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Float, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from db import session, engine


Base = declarative_base()

class StuGroup(Base):
     __tablename__ = "stu_groups"
     id = Column(Integer, primary_key = True)
     group_number = Column(String(10))
     kurs = Column(Integer)
     daytime = Column(Integer)
     created_at = Column(DateTime, server_default=func.now())
     last_update_at = Column(DateTime, server_default=func.now())


class Student(Base):
     __tablename__ = "students"
     id = Column(Integer, primary_key = True)
     full_name = Column(String(150))
     age = Column(Integer)
     email = Column(String(100))
     phone = Column(String(100))
     budget = Column(Boolean)
     scholarship = Column(Boolean)
     created_at = Column(DateTime, server_default=func.now())
     last_update_at = Column(DateTime, server_default=func.now()) 
     group_id = Column(Integer, ForeignKey("stu_groups.id", onupdate="CASCADE",ondelete="SET NULL"))

class Teacher(Base):
     __tablename__ = "teachers"
     id = Column(Integer, primary_key = True)
     full_name = Column(String(150))
     age = Column(Integer)
     email = Column(String(100))
     phone = Column(String(100)) #UNIQUE NOT NULL
     date_start_work = Column(Date)
     scientific_degree = Column(String(30))
     salary = Column(Float)
     created_at = Column(DateTime, server_default=func.now())
     last_update_at = Column(DateTime, server_default=func.now()) 


class Subject(Base):
     __tablename__ = "subjects"
     id = Column(Integer, primary_key = True)
     title = Column(String(100))
     created_at = Column(DateTime, server_default=func.now())
     last_update_at = Column(DateTime, server_default=func.now())
     teacher_id = Column(Integer, ForeignKey("teachers.id", onupdate="CASCADE",ondelete="SET NULL"))



class Grade(Base):
     __tablename__ = "grades"
     id = Column(Integer, primary_key = True)
     date_create = Column(Date)
     grade = Column(String(1))
     number_grade = Column(Integer)
     created_at = Column(DateTime, server_default=func.now())
     last_update_at = Column(DateTime, server_default=func.now())
     student_id = Column(Integer, ForeignKey("students.id", onupdate="CASCADE",ondelete="SET NULL"))
     subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE",ondelete="SET NULL"))


Base.metadata.create_all(engine)
Base.metadata.bind = engine