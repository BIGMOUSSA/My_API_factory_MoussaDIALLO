from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import sqlalchemy

load_dotenv()

# Récupérer les paramètres de connexions

def getParam():
    return {
        "user":os.environ.get('USER'),
        "password":os.environ.get('PASSWORD'),
        "database":os.environ.get('DATABASE')
    }

# configuration de la connexion

sql_database_url = "mysql://"+os.environ.get('USER')+":"+os.environ.get('PASSWORD')+"@localhost:3306/"+os.environ.get('DATABASE')

# établir la connexion 

engine = sqlalchemy.create_engine(
    sql_database_url) 

# Si la base existe déja ne pas créer et poursuivre
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()

if __name__ == '__main__':
    print(getParam())
    print(sql_database_url)
