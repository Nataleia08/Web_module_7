from db import session
from models import Student, Teacher, Grade, Subject, StuGroup
from sqlalchemy import func, all_

#-------------------Group------------------------

def create_group(gr_number):
    try:
        id_g = session.query(func.count(StuGroup.id)).select_from(StuGroup)+1
        group = StuGroup(id = id_g, group_number = gr_number, kurs = 1, created_at = func.now(), last_update_at = func.now())
        session.add(group)
        session.commit()
    except MemoryError as Err:
        print(Err)


def read_group():
    result = session.query(all_).select_from(StuGroup)
    print(result)

def update_group(id_g, gr_number):
    pass

def delete_group():
    pass

#----------------------Student---------------------

def create_student():
    pass

def read_student():
    result = session.query(all_).select_from(Student)
    print(result)

def update_student():
    pass

def delete_student():
    pass

#----------------Teacher----------------------------

def create_teacher():
    pass

def read_teacher():
    result = session.query(all_).select_from(Teacher)
    print(result)

def update_teacher():
    pass

def delete_teatcher():
    pass

#-----------------------------Subject-------------------------

def create_subject():
    pass

def read_subject():
    result = session.query(all_).select_from(Subject)
    print(result)

def update_subject():
    pass

def delete_subject():
    pass


#-------------------Grade---------------------------------

def create_grade():
    pass

def read_grade():
    result = session.query(all_).select_from(Grade)
    print(result)

def update_grade():
    pass

def delete_grade():
    pass
