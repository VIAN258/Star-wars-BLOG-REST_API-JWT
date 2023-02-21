import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True )
    password = db.Column(db.String(250), nullable=False)
    

    def __init__(self, name, email, password):
        self.email = email
        self.password = password
        self.name = name


class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    planet_name = db.Column(String(250))
   

class Ship(db.Model):
    __tablename__ = 'ship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(250))
   

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    characters_name = db.Column(String(250))
  

class Favorite(db.Model):
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
    
 
class Type(db.Model):
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
##render_er(Base, 'diagram.png')