from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddPupForm(FlaskForm):

    name = StringField('Enter name of the pup')
    age = IntegerField('Enter age of the pup')
    submit = SubmitField('Add Puppy')

class DelPupForm(FlaskForm):
    id = IntegerField('Id number of Puppy to remove')
    submit = SubmitField('Remove Puppy')

class AddOwner(FlaskForm):
    name = StringField('Name of the owner')
    id = IntegerField('Id of the puppy')
    submit = SubmitField('Add Owner')