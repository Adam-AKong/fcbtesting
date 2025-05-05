from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, DateTime, func

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now)

    # I don't believe we need any constraints here
    # __table_args__ = (
        
    # ) 
    
class C_Review(Base):
    __tablename__ = "c_review"
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    char_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    comment = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=func.now)
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # ) 
    
class F_Review(Base):
    __tablename__ = "f_review"
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    franchise_id = Column(Integer, ForeignKey('franchise.id'), nullable=False)
    comment = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=func.now)
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # )  
    
class Character(Base):
    __tablename__ = "character"
    
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False) 
    name = Column(String(30), nullable=False)
    description = Column(String(150), nullable=True)
    rating = Column(Float, nullable=False)
    strength = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    health = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now)
    
    # __table_args__ = (
    #     # maybe add constraints to rating, strength, speed, health
    #     # Need to discuss this together as group
    # ) 
    
class CharFran(Base):
    __tablename__ = "char_fran"
    
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey('character.id'), nullable=False) 
    franchise_id = Column (Integer, ForeignKey('franchise.id'), nullable=False) 
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # )
    
class Franchise(Base):
    __tablename__ = "franchise"
    
    id = Column(Integer, primary_key=True) 
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    
    # I don't believe we need any constraints here   
    # __table_args__ = (
        
    # ) 
    
class Battle(Base):
    __tablename__ = "battle"

    id = Column(Integer, primary_key=True)      
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)     
    char1_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    char2_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    vote1 = Column(Integer, default = 0)
    vote2 = Column(Integer, default = 0)
    winner_id = Column(Integer, ForeignKey('character.id'), nullable=False) # How to set winner for a tie / no winners?
    # start date
    # end date
    
    # __table_args__ = (
    #     # maybe we might need another table to actually store the votes
    #     # that way users can't vote more than once
    #       # vic: seconding this, but as a many:many table with a composite key
    #       # to be able to see where a user has voted + how many votes a battle
    #       # has
    # )   
    
