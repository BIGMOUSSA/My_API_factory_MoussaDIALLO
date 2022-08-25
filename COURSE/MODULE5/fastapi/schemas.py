from pydantic import BaseModel



class PeopleBase(BaseModel):
    id : int
    name : str
    phone : str
    email : str
    address : str
    latlng : str
    salary : float
    age : int 
    Device : str
    salary_XOF : float
    Coontry : str
    Flag : str
    class Config:
        orm_mode = True


