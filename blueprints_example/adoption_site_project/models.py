from adoption_site_project import db

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    #one-one relationship with Owner
    owner = db.relationship('Owner', backref ='puppy', uselist=False)

    def __init__(self, name, age) -> None:
        self.age = age
        self.name = name
    
    def __repr__(self) -> str:
        if self.owner:
            return "ID: {self.id}, Puppy Name: {self.name}, Age:{self.age}, Owner: {self.owner.name}"
        else:
            return "ID: {self.id}, Puppy Name: {self.name}, Age:{self.age}, Owner: None"


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id) -> None:
            self.name = name
            self.puppy_id = puppy_id
    
    