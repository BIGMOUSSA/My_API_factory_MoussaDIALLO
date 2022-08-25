from winreg import ConnectRegistry
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float,Text
from sqlalchemy.orm import relationship

from database import Base


class People(Base):
    __tablename__ = "People"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    latlng = Column(String(255))
    salary = Column(Float)
    age = Column(Integer)
    Device = Column(String(255))
    salary_XOF = Column(Float)
    Coontry =  Column(String(255))
    Flag =  Column(String(255))
    #email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)
    #items = relationship("Item", back_populates="owner")

