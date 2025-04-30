from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()

class User(Base):
    __table__name__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    # Figure out how to do Join Date
    
    __table_args__ = (
        
    ) 
    
class C_Review(Base):
    __table__name__ = 'c_review'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id')) 
    
    __table_args__ = (
        
    ) 
    
class F_Review(Base):
    __table__name__ = 'f_review'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))  
    
    __table_args__ = (
        
    ) 
    
class Character(Base):
    __table__name__ = 'character'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id')) 
    
    __table_args__ = (
        
    ) 
    
    
class Franchise(Base):
    __table__name__ = 'franchise'
    
    id = Column(Integer, primary_key=True) 
    
    __table_args__ = (
        
    ) 
    
class Battle(Base):
    __table__name__ = 'battle'
    
    id = Column(Integer, primary_key=True)      
    user_id = Column (Integer, ForeignKey('user.id'))     
    
    __table_args__ = (
        
    )   
    