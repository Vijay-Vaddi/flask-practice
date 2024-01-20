from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField('Enter name of the pup')
    age = IntegerField('Enter age of the pup')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Id number of Puppy to remove')
    submit = SubmitField('Remove Puppy')

