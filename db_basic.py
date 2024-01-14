import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class Base(DeclarativeBase):
#     pass

db = SQLAlchemy()  
db.init_app(app)

class Puppy(db.Model):
    # __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Puppy {self.name} is {self.age} years old "

if __file__ == '__main__': 
    app.run(debug=True)
