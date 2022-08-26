from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import sqlalchemy
import pymysql

load_dotenv()

# Récupérer les paramètres de connexions


user = os.environ.get('USER')
password= os.environ.get('PASSWORD')
database = "scraping"
db_hoste = "localhost"
db_port =  "3306"

# configuration de la connexion

sql_database_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(user, password,db_hoste,db_port,database)

# établir la connexion 

engine = sqlalchemy.create_engine(
    sql_database_url) 

# Si la base existe déja ne pas créer et poursuivre

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()

