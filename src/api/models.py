from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False )
    email = db.Column(db.String(120), unique=True, nullable=False )
    password = db.Column(db.String(80), nullable=False)
    

    def serialize (self):
        return{
            "id": self.id,
            "name": self.name,
            "email": self.email,
           
        }
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f" {self.id}: {self.name}: {self.email}: {self.password}"

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250))

    def serialize (self):
        return{
            "id": self.id,
            "planet_name": self.planet_name,           
        }
    
    def __init__(self, planet_name):
        self.planet_name = planet_name
    
    def __repr__(self):
        return f" {self.id}: {self.planet_name}" 

class Ship(db.Model):
    __tablename__ = 'ship'
    id = db.Column(db.Integer, primary_key=True)
    ships_name = db.Column(db.String(250))

    def serialize (self):
        return{
            "id": self.id,
            "ship_name": self.ship_name,           
        }
    
    def __init__(self, ship_name):
        self.ship_name = ship_name
    
    def __repr__(self):
        return f" {self.id}: {self.ship_name}" 


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))

    def serialize (self):
        return{
            "id": self.id,
            "character_name": self.charcater_name,           
        }
    
    def __init__(self, charcter_name):
        self.character_name = character_name
    
    def __repr__(self):
        return f" {self.id}: {self.character_name}" 


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    character = db.relationship(Character)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    planet = db.relationship(Planet)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'), nullable=False)
    ship = db.relationship(Ship)
    

    def serialize (self):
        return{
            "id": self.id,
            "user_id": self.user_id, 
            "character_id": self.character_id, 
            "planet_id": self.planet_id,
            "ship_id": self.ship_id,           
        }
    
    def __init__(self, user_id, character_id, planet_id, ship_id):
        self.user_id = user_id
        self.character_id = character_id
        self.planet_id = planet_id
        self.ship_id = ship_id
    
    def __repr__(self):
        return f" {self.id}: {self.user_id}: {self.character_id}: {self.planet_id}: {self.ship_id}:" 
     
        
        


    

    

















