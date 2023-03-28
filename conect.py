from datetime import datetime
from psycopg2 import connect, Error
from contextlib import contextmanager

@contextmanager
def new_connect():
    conn = None
    try:
        conn = connect(host = 'localhost', user = 'postgres', password = '112233445566', port = 5432)
        yield conn
    except Error as err:
        print("Error:", err)
        # conn.rollback()
    finally:
        if conn:
            conn.close()



# def create_table():
#         with new_connect() as conn:
#             c = conn.cursor()
#             c.execute(sql)
#             conn.commit()
#             c.close()