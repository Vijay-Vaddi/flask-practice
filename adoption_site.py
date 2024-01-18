import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddPupForm, DelPupForm, AddOwner

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

    owner = db.relationship('Owner', backref = 'puppy', uselist = False)

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        if self.owner:
            return f"Puppy {self.name} is {self.age} years old and {self.owner.name} is the owner"
        else:
            return f"{self.id} Puppy  {self.name}  is {self.age} and has no owner yet"
        
class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id) -> None:
        self.name = name
        self.puppy_id = puppy_id


#########################################
###### VIEW FUNCTIONS- HAVE FORMS #######
#########################################
    
@app.route('/')
def index():

    return render_template('adoption_site/index.html' )


@app.route('/add', methods = ['GET', 'POST'])
def add_pup():
    
    form = AddPupForm()
    
    #add to database and show list of puppies 
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        new_pup = Puppy(name, age)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    # add puppy default view
    return render_template("adoption_site/add.html", form = form)

@app.route('/list')
def list_pup():
 
    puppies = Puppy.query.all()
    return render_template('adoption_site/list_of_pups.html', puppies=puppies)


@app.route('/delete', methods= ['GET', 'POST'])
def del_pup():
    
    form = DelPupForm() 
    
    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        # pup = db.session.get(Puppy, form.id.data) why not this?
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("list_pup"))
    
    return render_template('adoption_site/delete.html', form=form)

@app.route('/add_owner', methods= ['GET', 'POST'])
def add_owner():

    form = AddOwner()

    if form.validate_on_submit():
        puppy_id = form.id.data
        name = form.name.data
        
        own = Owner(name, puppy_id)
        db.session.add(own)
        db.session.commit()
        return redirect(url_for('list_pup'))
    
    return render_template('adoption_site/add_owner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



     



