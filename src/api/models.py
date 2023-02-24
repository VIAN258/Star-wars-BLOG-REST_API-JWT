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


    

    

















