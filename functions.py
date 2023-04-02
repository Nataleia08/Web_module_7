from db import session
from models import Student, Teacher, Grade, Subject, StuGroup
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#-------------------Group------------------------

def create_group(gr_number):
    try:
        id_g = int(session.query(func.count(StuGroup.id)).select_from(StuGroup).scalar())+1
        group = StuGroup(id=id_g, group_number=gr_number, kurs=1, created_at=func.now(), last_update_at=func.now())
        session.add(group)
        session.commit()
    except IntegrityError as Err:
        print(Err)

def read_group():
    try:
        result = session.query(StuGroup).all()
        print("ID, Group number, kurs, daytime")
        for g in result:
            print(g.id, g.group_number, g.kurs, g.daytime)
    except:
        print("Some error!")


def update_group(id_g, gr_number):
    try:
        new_group = session.query(StuGroup).get(id_g)
        new_group.group_number = gr_number
        new_group.last_update_at = func.now()
        session.add(new_group)
        session.commit()
    except:
        print("Some error!")


def delete_group(id_g):
    try:
        new_group = session.query(StuGroup).get(id_g)
        session.delete(new_group)
        session.commit()
    except:
        print("Some error!")

#----------------------Student---------------------

def create_student(name):
    try:
        id_s = int(session.query(func.count(Student.id)).select_from(Student).scalar())+1
        new_student = Student(id=id_s, full_name=name,  age = 18, created_at=func.now(), last_update_at=func.now())
        session.add(new_student)
        session.commit()
    except IntegrityError as Err:
        print(Err)

def read_student():
    try:
        result = session.query(Student).all()
        print("Id, Name, Age, Email, Phone")
        for r in result:
            print(r.id, r.full_name, r.age, r.email, r.phone)
    except:
        print("Some error!")

def update_student(id_s, name):
    try:
        new_student = session.query(Student).get(id_s)
        new_student.full_name = name
        new_student.last_update_at = func.now()
        session.add(new_student)
        session.commit()
    except:
        print("Some error!")


def delete_student(id_s):
    try:
        d_student = session.query(Student).get(id_s)
        session.delete(d_student)
        session.commit()
    except:
        print("Some error!")


#----------------Teacher----------------------------

def create_teacher(name):
    try:
        id_s = int(session.query(func.count(Teacher.id)).select_from(Teacher).scalar()) + 1
        new_teacher = Teacher(id=id_s, full_name=name,  age = 18, salary= 0, date_start_work=datetime.now().date(), created_at=func.now(), last_update_at=func.now())
        session.add(new_teacher)
        session.commit()
    except IntegrityError as Err:
        print(Err)

def read_teacher():
    try:
        result = session.query(Teacher).all()
        print("Id, Name, Age, Email, Phone")
        for r in result:
            print(r.id, r.full_name, r.age, r.email, r.phone)
    except:
        print("Some error!")


def update_teacher(id_t, name):
    try:
        new_teacher = session.query(Teacher).get(id_t)
        new_teacher.full_name = name
        new_teacher.last_update_at = func.now()
        session.add(new_teacher)
        session.commit()
    except:
        print("Same error!")


def delete_teacher(id_t):
    try:
        d_teacher = session.query(Teacher).get(id_t)
        session.delete(d_teacher)
        session.commit()
    except:
        print("Same error!")


#-----------------------------Subject-------------------------

def create_subject(title_s):
    try:
        id_s = int(session.query(func.count(Subject.id)).select_from(Subject).scalar()) + 1
        new_subject = Subject(id=id_s, title=title_s, created_at=func.now(), last_update_at=func.now())
        session.add(new_subject)
        session.commit()
    except IntegrityError as Err:
        print(Err)

def read_subject():
    try:
        result = session.query(Subject).all()
        print("Id, Title")
        for r in result:
            print(r.id, r.title)
    except:
        print("Same error!")


def update_subject(id_s, title_s):
    try:
        new_subject = session.query(Subject).get(id_s)
        new_subject.title = title_s
        new_subject.last_update_at = func.now()
        session.add(new_subject)
        session.commit()
    except:
        print("Some error!")



def delete_subject(id_s):
    try:
        d_subject = session.query(Subject).get(id_s)
        session.delete(d_subject)
        session.commit()
    except:
        print("Some error!")



#-------------------Grade---------------------------------

def create_grade(number_g):
    try:
        id_g = int(session.query(func.count(Grade.id)).select_from(Grade).scalar()) + 1
        new_grade = Grade(id = id_g, number_grade=number_g, date_create = func.now(), created_at=func.now(), last_update_at=func.now())
        session.add(new_grade)
        session.commit()
    except IntegrityError as Err:
        print(Err)

def read_grade():
    try:
        result = session.query(Grade.id, Grade.number_grade, Grade.date_create, Student.full_name, Subject.title). \
            select_from(Grade).join(Student).join(Subject).all()
        print("Id, Grade, Number of grade, Date, Student, Subject")
        for r in result:
            print(r)
    except:
        print("Some error!")


def update_grade(id_g, number_g):
    try:
        new_grade = session.query(Grade).get(id_g)
        new_grade.number_grade = number_g
        new_grade.last_update_at = func.now()
        session.add(new_grade)
        session.commit()
    except:
        print("Some error!")


def delete_grade(id_g):
    try:
        d_grade = session.query(Grade).get(id_g)
        session.delete(d_grade)
        session.commit()
    except:
        print("Some error!")

