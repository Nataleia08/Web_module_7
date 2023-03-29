import configparser
import pathlib

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

file_config = pathlib.Path(__file__).parent.joinpath('confih.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get("DEV_DB", "USER")
password = config.get("DEV_DB", "PASSWORD")
domain = config.get("DEV_DB", "DOMAIN")
port = config.get("DEV_DB", "PORT")
database = config.get("DEV_DB", "DB_NAME")

url = f"postgresql://{username}:{password}@{domain}:{port}/{database}"

engine = create_engine(url, echo = True)
session = sessionmaker(bind=engine)