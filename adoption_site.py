import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello123'

#######################################
########## SQL DATABASE SECTION #######
#######################################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'adoption_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
Migrate(app,db)
#####################
#### MODELS #########
#####################


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    toys = db.relationship('toy', backref = 'puppies', lazy = 'dynamic')

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return f"Puppy {self.name} is {self.age} years old"
    


