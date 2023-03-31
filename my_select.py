from db import session
from models import Student, Teacher, Grade, Subject, StuGroup
from sqlalchemy import func, desc, distinct

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

def select_2():
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject)\
            .select_where(Subject.id == 1).group_by(Student.id)\
                .order_by(desc('avg_grade'))
    return result

def select_3():
    """Знайти середній бал у групах з певного предмета."""
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).join(StuGroup)\
            .select_where(Subject.id == 1).group_by(StuGroup.id).order_by(desc('avg_grade'))
    return result

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade)
    return result

def select_5():
    """Знайти які курси читає певний викладач."""
    result = session.query(Subject.title, Teacher.full_name)\
        .select_from(Subject).join(Teacher).select_where(Teacher.id ==1)
    return result

def select_6():
    """Знайти список студентів у певній групі."""
    result = session.query(StuGroup.group_number, Student.full_name)\
        .select_from(Student).join(StuGroup)\
            .select_where(StuGroup.id == 1)
    return result

def select_7():
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query(Student.full_name, Grade.number_grade, Grade.grade, StuGroup.group_number, Grade.date_create, Subject.title)\
        .select_from(Grade).join(Student).join(StuGroup).join(Subject)\
        .select_where((Grade.subject_id == 1)and(Student.id == 1))
    return result

def select_8():
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query(Subject.title, func.avg(Grade.number_grade))\
        .select_from(Grade).join(Subject).join(Teacher)\
            .select_where(Teacher.id == 1).group_by(Subject.id == 1)
    return result

def select_9():
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query(Subject.title.distinct).select_from(Subject).join(Grade).join(Student).select_where(Student.id == 1)
    return result

def select_10():
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query(Subject.title.distinct).select_from(Subject).join(Teacher).join(Grade).join(Student)\
        .select_where((Teacher.id == 1) and (Student.id == 1))
    return result

def select_11():
    """Середній бал, який певний викладач ставить певному студентові."""
    result = session.query(func.avg(Grade.grade)).select_from(Grade).\
        join(Student).join(Subject).join(Teacher).select_where((Teacher.id == 1)and(Student.id == 1)).group_by(Grade.student_id)
    return result

def select_12():
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    result = session.query(Grade.number_grade, Student.full_name).select_from(Grade).\
        join(Student).join(Subject).join(StuGroup).select_where((StuGroup.id == 1)and(Subject.id == 1)and(Grade.date_create > '2023-02-20'))
    return result

if __name__ == "__main__":
    n = input("Input number of function>>>>")
    match n:
        case 1: select_1()
        case 2: select_2()
        case 3: select_3()
        case 4: select_4()
        case 5: select_5()
        case 6: select_6()
        case 7: select_7()
        case 8: select_8()
        case 9: select_9()
        case 10: select_10()
        case 11: select_11()
        case 12: select_12()