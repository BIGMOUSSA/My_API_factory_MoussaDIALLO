from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
#import pymysql
import sqlalchemy
sql_database_url = 'mysql://root:root@localhost:3306/scraping'
engine = sqlalchemy.create_engine(
    sql_database_url) 
if not database_exists(engine.url):
    create_database(engine.url)
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
