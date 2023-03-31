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
    result = session.query(StuGroup).all()
    print(result)

def update_group(id_g, gr_number):
    new_group = session.query(StuGroup).get(id_q)
    new_group.group_number = gr_number
    session.add(new_group)
    session.commit()

def delete_group():
    new_group = session.query(StuGroup).get(id_q)
    session.delete()
    session.comit()

#----------------------Student---------------------

def create_student():
    pass

def read_student():
    result = session.query(Student).all()
    print(result)

def update_student():
    pass

def delete_student():
    pass

#----------------Teacher----------------------------

def create_teacher():
    pass

def read_teacher():
    result = session.query(Teacher).all()
    print(result)

def update_teacher():
    pass

def delete_teatcher():
    pass

#-----------------------------Subject-------------------------

def create_subject():
    pass

def read_subject():
    result = session.query(Subject).all()
    print(result)

def update_subject():
    pass

def delete_subject():
    pass


#-------------------Grade---------------------------------

def create_grade():
    pass

def read_grade():
    result = session.query(Grade).all()
    print(result)

def update_grade():
    pass

def delete_grade():
    pass
