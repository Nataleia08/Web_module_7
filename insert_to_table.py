from faker import Faker
from random import randint, choice 
from execute_script_first import new_connect
from datetime import datetime, timedelta
from psycopg2 import connect
import random
from contextlib import contextmanager


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



if __name__ == "__main__":

    sql_2 = """INSERT INTO stu_groups (id, group_number, kurs, daytime) VALUES (%s, %s, %s, %s)"""

    with new_connect() as conn:
        c = conn.cursor()
        j = 1
        for i in GROUP_LIST:
            c.execute(sql_2, (j, i, randint(1, 5), randint(1, 2)))
            conn.commit()
            j +=1 
        c.close()


    sql_3 = """INSERT INTO students (id, full_name, age, email, phone, budget, scholarship, group_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    with new_connect() as conn:
        c = conn.cursor()
        for i in range(50):
            c.execute(sql_3, (i+1, fake.name(), randint(18, 30), fake.email(), fake.phone_number(), bool(randint(0, 1)), bool(randint(0, 1)), choice(range(1, 4))))
            conn.commit()
        c.close()


    sql_4 = """INSERT INTO teachers (id, full_name, age, email, phone, date_start_work, scientific_degree, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    with new_connect() as conn:
        c = conn.cursor()
        for i in range(6):
            c.execute(sql_4, (i+1, fake.name(), randint(35, 90), fake.company_email(), fake.phone_number(), random_date(datetime(year=2013, month=1, day=1), datetime(year=2023, month=1, day=1)), choice(scientific_degree_list),  randint(20000, 50000)))
            conn.commit()
        c.close()

    sql_5 = """INSERT INTO subjects (id, title, teacher_id) VALUES (%s, %s, %s)"""

    with new_connect() as conn:
        c = conn.cursor()
        j = 1
        for i in SUBJECT_LIST:
            c.execute(sql_5, (j, i, choice(range(1, 5))))
            conn.commit()
            j += 1
        c.close()     

    sql_6 = """INSERT INTO grades (id, date_create, grade, number_grade, student_id, subject_id) VALUES (%s, %s, %s, %s, %s, %s)"""

    with new_connect() as conn:
        c = conn.cursor()
        j = 1
        for s in range(50):
            for g in range(20):
                c.execute(sql_6, (j, random_date(datetime(year=2022, month=9, day=1), datetime(year=2023, month=3, day=24)), choice(GRADE_LIST), randint(30, 100), s+1, randint(1, 7)))
                conn.commit()
                j += 1
        c.close()