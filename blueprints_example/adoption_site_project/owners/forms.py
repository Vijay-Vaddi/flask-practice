from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddOwnerForm(FlaskForm):
    name = StringField('Name of the owner')
    id = IntegerField('Id of the puppy')
    submit = SubmitField('Add Owner')