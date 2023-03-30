from db import session
from models import Student, Teacher, TeacherStudent, Grade, Subject, StuGroup

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query()
    return result

def select_2():
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query()
    return result

def select_3():
    """Знайти середній бал у групах з певного предмета."""
    result = session.query()
    return result

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query()
    return result

def select_5():
    """Знайти які курси читає певний викладач."""
    result = session.query()
    return result

def select_6():
    """Знайти список студентів у певній групі."""
    result = session.query()
    return result

def select_7():
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query()
    return result

def select_8():
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query()
    return result

def select_9():
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query()
    return result

def select_10():
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query()
    return result

def select_dop_1():
    """Середній бал, який певний викладач ставить певному студентові."""
    result = session.query()
    return result

def select_dop_2():
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    result = session.query()
    return result