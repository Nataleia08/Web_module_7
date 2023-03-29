from faker import Faker
from random import randint, choice 
from datetime import datetime, timedelta
from psycopg2 import connect
import random
from contextlib import contextmanager
import sqlalchemy

from db import session
from models import Student, Teacher, TeacherStudent, Grade, Subject, StuGroup

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
    pass


def insert_students():
    for _ in range(100):
        student = Student(
            full_name = fake.name(),
            age = fake.age(18, 25), 
            email = fake.email(), 
            phone = fake.phone_number(), 
            budget = randint(0, 1), 
            scholarship = randint(0, 1), 
            created_at  = datetime.now()
            last_update_at = datetime.now()
            group_id = randint(1, 3)
        )
        session.add(student)
    session.commit()

def insert_teachers():
    pass

def insert_subjects():
    pass



def insert_grades():
    pass

def insert_links():
    pass


if __name__ == "__main__":
    try:
        insert_students()
        insert_group()
        insert_subjects()
        insert_teachers()
        insert_grades()
    except SQLAlchemyError as err:
        print(err)
    