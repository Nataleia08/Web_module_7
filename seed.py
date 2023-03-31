from faker import Faker
from random import randint, choice 
from datetime import datetime, timedelta
# from psycopg2 import connect
# import random
# from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError

from db import session
from models import Student, Teacher, Grade, Subject, StuGroup

fake = Faker("uk-UA")

GROUP_LIST = ["КА-56", "МА-98", "СА-33"]

STUDENTS_COUNT = 200
SUBJECT_LIST = [
    "Математичний аналіз", 
    "Лінейна алгебра", 
    "Теорія ймовірностей",
    "Алгоритми програмування",
    "Операційні системи",
    "Дискретна математика",
    "Чисельні методи"
]

scientific_degree_list = [
    "Доцент",
    "Аспирант", 
    "Професор",
    "Доктор наук",
    "Старший дослідник"
]

GRADE_LIST = [
    "A", 
    "B", 
    "C", 
    "D",
    "F"
]

def random_date(date_start: datetime, date_end: datetime):
    date_list = [date_start]
    res_date = date_start
    while res_date!= date_end:
        res_date += timedelta(days=1)
        date_list.append(res_date)
    result = choice(date_list)
    return result

def insert_group():
    j = 1
    for i in GROUP_LIST:
        group = StuGroup(
            id = j, 
            group_number = i, 
            kurs = randint(1, 5), 
            daytime = randint(1, 2), 
            created_at = datetime.now(), 
            last_update_at = datetime.now())
        session.add(group)
        j +=1
    session.commit()
   


def insert_students():
    for i in range(100):
        student = Student (
            id = i, 
            full_name = fake.name(),
            age = randint(18, 25),
            email = fake.email(), 
            phone = fake.phone_number(), 
            budget = randint(0, 1), 
            scholarship = randint(0, 1), 
            created_at  = datetime.now(),
            last_update_at = datetime.now(),
            group_id = randint(1, 3) )
        session.add(student)
    session.commit()


def insert_teachers():
    for i in range(6):
        teacher = Teacher(
            id = i+1, 
            full_name = fake.name(), 
            age = randint(35, 90), 
            email = fake.company_email(), 
            phone = fake.phone_number(), 
            date_start_work = random_date(datetime(year=2013, month=1, day=1), datetime(year=2023, month=1, day=1)), 
            scientific_degree = choice(scientific_degree_list),  
            salary = randint(20000, 50000), 
            created_at  = datetime.now(),
            last_update_at = datetime.now())
        session.add(teacher)
    session.commit()



def insert_subjects():
    j = 1
    for i in SUBJECT_LIST:
        subject = Subject(
            id = j,
            title = i,
            created_at  = datetime.now(),
            last_update_at = datetime.now(), 
            teacher_id = choice(range(1, 5))
        )
        session.add(subject)
        j += 1
    session.commit()



def insert_grades():
    j = 1
    for s in range(50):
        for g in range(20):
            grade = Grade(
                id = j, 
                date_create = random_date(datetime(year=2022, month=9, day=1), datetime(year=2023, month=3, day=24)), 
                grade = choice(GRADE_LIST), 
                number_grade = randint(30, 100), 
                last_update_at = datetime.now(),
                student_id = s+1, 
                subject_id = randint(1, 7)
            )
            session.add(grade)
            j += 1
    session.commit()


if __name__ == "__main__":
    try:
        insert_group()
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_grades()
    except SQLAlchemyError as err:
        print(err)
    