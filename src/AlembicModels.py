from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, ForeignKey, Integer, String

Base = declarative_base()

class User(Base):
    __table__name__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    # join date
    
    # I don't believe we need any constraints here
    # __table_args__ = (
        
    # ) 
    
class C_Review(Base):
    __table__name__ = 'c_review'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    char_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    comment = Column(String(500), nullable=False)
    # creation date
 
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # ) 
    
class F_Review(Base):
    __table__name__ = 'f_review'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    franchise_id = Column(Integer, ForeignKey('franchise.id'), nullable=False)
    comment = Column(String(500), nullable=False)
    # creation date
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # )  
    
class Character(Base):
    __table__name__ = 'character'
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False) 
    name = Column(String(30), nullable=False)
    franchise_id = Column (Integer, ForeignKey('franchise.id'), nullable=False) 
    description = Column(String(150), nullable=True)
    rating = Column(Float, nullable=False)
    strength = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    health = Column(Float, nullable=False)
    # creation date
    
    __table_args__ = (
        # maybe add constraints to rating, strength, speed, health
        # Need to discuss this together as group
    ) 
    
    
class Franchise(Base):
    __table__name__ = 'franchise'
    
    id = Column(Integer, primary_key=True) 
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # ) 
    
class Battle(Base):
    __table__name__ = 'battle'
    
    id = Column(Integer, primary_key=True)      
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)     
    char1_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    char2_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    vote1 = Column(Integer, default = 0)
    vote2 = Column(Integer, default = 0)
    winner_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    # start date
    # end date
    
    __table_args__ = (
        # maybe we might need another table to actually store the votes
        # that way users can't vote more than once
    )   
    