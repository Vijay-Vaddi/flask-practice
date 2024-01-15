from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data_relation.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push() 
Migrate(app, db)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    toys = db.relationship('Toy', backref = 'puppy', lazy = 'dynamic')
    # one to many, one puppy to many toys relationship
    #both front and back reference to show relationship with toy model. 
    #lazy, how the related items are loaded. instead of loded the related items, the query that can load them is given

    owner = db.relationship('Owner', backref = 'puppy', uselist = False)
    # use LIST is true by default because by default its true, which makes ssense for one to many 
    # since one puppy can have multi toys, but in one to one relation like one owner to one puppy, its false.   
    
    def __init__(self, name, age, toys) -> None:
        self.name = name
        self.age = age
        # self.toys = toys #not added
    def __repr__(self) -> str:
        # if puppy has owner
        if self.owner:
            return f"Puppy name is {self.name} and the owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"
        
    def report_toys(self):
        print(f"Puppy has toys {self.toys}")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))
    # set primary key of another table as foreign key 

    def __init__(self,item_name, puppy_id) -> None:
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id) -> None:
        
        self.name = name
        self.puppy_id = puppy_id

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)



