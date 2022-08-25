
from enum import Flag
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models import People
from sqlalchemy.ext.declarative import declarative_base
from database import sql_database_url
import pandas as pd


engine = create_engine(
    sql_database_url,echo=False)

Session = sessionmaker(bind=engine)
session=Session()

Base = declarative_base()



empdata = pd.read_csv("COURSE/DATABASES/Final_data.csv",index_col=0, delimiter = ',')
empdata.fillna("",inplace=True)



def GoSaveData(files:pd.DataFrame):

    #loop through the data frame
    
    for i,row in files.iterrows():
        data= tuple(row)

        student1 = People(
            name=data[0],
            phone=data[1],
            email=data[2],
            address=data[3],
            latlng=data[4],
            salary=data[5],
            age=data[6],
            Device=data[7],
            salary_XOF=data[8],
            Coontry=data[9],
            Flag=data[10])
        session.add(student1)
        session.commit()
        print("Record inserted")

GoSaveData(empdata)


