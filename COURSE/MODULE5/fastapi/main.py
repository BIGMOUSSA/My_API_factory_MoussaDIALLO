from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

import  models
import  schemas
from database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

 
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_People(db: Session):
    return db.query(models.People).all()

@app.get("/People", response_model=List[schemas.PeopleBase],status_code=200)
def read_people(db: Session = Depends(get_db)):
    Peoples = db.query(models.People).all()
    return Peoples



