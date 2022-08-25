from database import Base,engine
from models import People
from sqlalchemy.dialects.mysql import insert
print("Creating database....")

Base.metadata.create_all(engine)

### ADDING DATA TO THE BASE

