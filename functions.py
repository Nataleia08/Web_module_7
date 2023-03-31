from db import session
from models import Student, Teacher, Grade, Subject, StuGroup
from sqlalchemy import func, all_

#-------------------Group------------------------

def create_group(gr_number):
    try:
        id_g = int(session.query(func.count(StuGroup.id)).select_from(StuGroup).scalar())+1
        group = StuGroup(id = id_g, group_number= gr_number, kurs= 1, created_at= func.now(), last_update_at= func.now())
        session.add(group)
        session.commit()
    except MemoryError as Err:
        print(Err)

def read_group():
    result = session.query(StuGroup).all()
    print("ID, Group number, kurs, daytime")
    for g in result:
        print(g.id, g.group_number, g.kurs, g.daytime)

def update_group(id_g, gr_number):
    new_group = session.query(StuGroup).get(id_g)
    new_group.group_number = gr_number
    session.add(new_group)
    session.commit()

def delete_group(id_g):
    new_group = session.query(StuGroup).get(id_g)
    session.delete(new_group)
    session.commit()

#----------------------Student---------------------

def create_student(name):
    try:
        id_s = session.query(func.count(Student.id)).select_from(Student)+1
        new_student = Student(id=id_s, full_name=name, created_at = func.now(), last_update_at = func.now())
        session.add(new_student)
        session.commit()
    except TypeError as Err:
        print(Err)

def read_student():
    result = session.query(Student).all()
    print("Id, Name, Age, Email, Phone")
    for r in result:
        print(r.id, r.full_name, r.age, r.email, r.phone)

def update_student(id_s, name):
    new_student = session.query(Student).get(id_s)
    new_student.full_name = name
    session.add(new_student)
    session.commit()

def delete_student(id_s):
    d_student = session.query(Student).get(id_s)
    session.delete(d_student)
    session.commit()

#----------------Teacher----------------------------

def create_teacher(name):
    try:
        id_s = int(list(session.query(func.count(Teacher.id)).select_from(Teacher))[0]) + 1
        new_teacher = Teacher(id=id_s, full_name=name, created_at=func.now(), last_update_at=func.now())
        session.add(new_teacher)
        session.commit()
    except TypeError as Err:
        print(Err)

def read_teacher():
    result = session.query(Teacher).all()
    print("Id, Name, Age, Email, Phone")
    for r in result:
        print(r.id, r.full_name, r.age, r.email, r.phone)

def update_teacher(id_t, name):
    new_teacher = session.query(Teacher).get(id_t)
    new_teacher.full_name = name
    session.add(new_teacher)
    session.commit()

def delete_teatcher(id_t):
    d_teacher = session.query(Teacher).get(id_t)
    session.delete(d_teacher)
    session.commit()

#-----------------------------Subject-------------------------

def create_subject(title_s):
    try:
        id_s = session.query(func.count(Subject.id)).select_from(Subject) + 1
        new_subject = Subject(id=id_s, title=title_s, created_at=func.now(), last_update_at=func.now())
        session.add(new_subject)
        session.commit()
    except TypeError as Err:
        print(Err)

def read_subject():
    result = session.query(Subject).all()
    print("Id, Title")
    for r in result:
        print(r.id, r.title)

def update_subject(id_s, title_s):
    new_subject = session.query(Subject).get(id_s)
    new_subject.title = title_s
    session.add(new_subject)
    session.commit()

def delete_subject(id_s):
    d_subject = session.query(Subject).get(id_s)
    session.delete(d_subject)
    session.commit()


#-------------------Grade---------------------------------

def create_grade(number_g):
    try:
        # id_g = int(session.query(func.count(Grade.id)).select_from(Grade)) + 1
        new_grade = Grade(number_grade=number_g, date_create = func.now(), created_at=func.now(), last_update_at=func.now())
        session.add(new_grade)
        session.commit()
    except TypeError as Err:
        print(Err)

def read_grade():
    result = session.query(Grade.id, Grade.number_grade, Grade.date_create, Student.full_name, Subject.title).\
        select_from(Grade).join(Student).join(Subject).all()
    print("Id, Grade, Number of grade, Date, Student, Subject")
    for r in result:
        print(r)

def update_grade(id_g, number_g):
    new_grade = session.query(Grade).get(id_g)
    new_grade.number_grade = number_g
    session.add(new_grade)
    session.commit()

def delete_grade(id_g):
    d_grade = session.query(Grade).get(id_g)
    session.delete(d_grade)
    session.commit()
