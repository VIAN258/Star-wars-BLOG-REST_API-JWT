import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    planet_name = db.Column(String(250))
   

class Ship(Base):
    __tablename__ = 'ship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(250))
   

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    characters_name = db.Column(String(250))
  

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    character_id = db.Column(Integer, ForeignKey('character.id'), nullable=False)
    character = relationship(Character)
    planet_id = db.Column(Integer, ForeignKey('planet.id'), nullable=False)
    planet = relationship(Planet)
    ship_id = db.Column(Integer, ForeignKey('ship.id'), nullable=False)
    ship = relationship(Ship)
    type_id = db.Column(Integer, ForeignKey('type.id'), nullable=False)
    
 
class Type(Base):
    __tablename__ = 'type'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    character_id = db.Column(Integer, ForeignKey('character.id'))
    planet_id = db.Column(Integer, ForeignKey('planet.id'))
    ship_id = db.Column(Integer, ForeignKey('ship.id'))
    
    
    
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')