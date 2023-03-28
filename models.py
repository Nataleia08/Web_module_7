from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

class StuGroups:
     id = Column(Integer, primary_key = True)
     group_number = Column(String(10))
     kurs = Column(Integer)
     daytime = Column(Integer)
     
     id INT PRIMARY KEY,
 group_number CHAR(10),
 kurs INT, 
 daytime INT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
 last_update_at TIMESTAMP