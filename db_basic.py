import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ , when a module is loaded in python, the __file__ is build it and set to the actual name of the file, ie basic.py
# os.path.dirname() grabs directory name
# abspath grabs the full path to the directory irrespective of the OS
# print(basedir)
app = Flask(__name__)

# sets the data base location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'+os.path.join(basedir,'data.sqlite')

#setting if to track all modification to the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# create a model class. Model is nothing but a table in db
# when you pass your app to SQLALCHEmy, the db will now have Model class
class Puppy(db.Model):
    # manual override to table name. default would be class name Puppy
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age

    # returns the string representation of database
    def __repr__(self) -> str:
        return f"Puppy {self.name} is {self.age} years old "



# testing new changes after auto save