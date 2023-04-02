from db import session
from models import Student, Teacher, Grade, Subject, StuGroup
from sqlalchemy import func, desc, distinct


def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query(Student.full_name, func.round(func.avg(Grade.number_grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    for i in result:
        print(i)

def select_2():
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query(Student.full_name, func.round(func.avg(Grade.number_grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject)\
            .where(Subject.id == 1).group_by(Student.id)\
                .order_by(desc('avg_grade')).first()
    for i in result:
        print(i)

def select_3():
    """Знайти середній бал у групах з певного предмета."""
    result = session.query(func.round(func.avg(Grade.number_grade), 2).label('avg_grade'), StuGroup.group_number)\
        .select_from(Grade).join(Student).join(Subject).join(StuGroup)\
            .where(Subject.id == 1).group_by(StuGroup.id).order_by(desc('avg_grade')).all()
    for i in result:
        print(i)

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.round(func.avg(Grade.number_grade), 2).label('avg_grade')).select_from(Grade).all()
    for i in result:
        print(i)

def select_5():
    """Знайти які курси читає певний викладач."""
    result = session.query(Subject.title, Teacher.full_name)\
        .select_from(Subject).join(Teacher).where(Teacher.id ==1).all()
    for i in result:
        print(i)

def select_6():
    """Знайти список студентів у певній групі."""
    result = session.query(StuGroup.group_number, Student.full_name)\
        .select_from(Student).join(StuGroup)\
            .where(StuGroup.id == 1).all()
    for i in result:
        print(i)

def select_7():
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query(Student.full_name, Grade.number_grade, Grade.grade, StuGroup.group_number, Grade.date_create, Subject.title)\
        .select_from(Grade).join(Student).join(StuGroup).join(Subject)\
        .where((Grade.subject_id == 1)and(Student.id == 1)).all()
    for i in result:
        print(i)

def select_8():
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query(Subject.title, func.avg(Grade.number_grade))\
        .select_from(Grade).join(Subject).join(Teacher)\
            .where(Teacher.id == 1).group_by(Subject.id).all()
    for i in result:
        print(i)

def select_9():
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query(func.distinct(Subject.title)).select_from(Subject).join(Grade).join(Student).where(Student.id == 2).all()
    for i in result:
        print(i)

def select_10():
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query(func.distinct(Subject.title)).select_from(Subject).join(Teacher).join(Grade).join(Student)\
        .where((Teacher.id == 1) and (Student.id == 1)).all()
    for i in result:
        print(i)

def select_11():
    """Середній бал, який певний викладач ставить певному студентові."""
    result = session.query(func.avg(Grade.number_grade)).select_from(Grade).\
        join(Student).join(Subject).join(Teacher).where(Teacher.id == 1).where(Student.id == 1).group_by(Student.id).all()
    for i in result:
        print(i)

def select_12():
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    result = session.query(Grade.number_grade, Student.full_name).select_from(Grade).\
        join(Student).join(Subject).join(StuGroup).where(StuGroup.id == 1).where(Subject.id == 1).where(Grade.date_create > '2023-03-15').all()
    for i in result:
        print(i)

if __name__ == "__main__":
    n = input("Input number of function>>>>")
    match n:
        case "1": select_1()
        case "2": select_2()
        case "3": select_3()
        case "4": select_4()
        case "5": select_5()
        case "6": select_6()
        case "7": select_7()
        case "8": select_8()
        case "9": select_9()
        case "10": select_10()
        case "11": select_11()
        case "12": select_12()