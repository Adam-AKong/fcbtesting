from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __table__name__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # Figure out how to do Join Date
    
# Create other Classes to import Tables into DB