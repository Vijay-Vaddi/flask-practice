from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                     RadioField, SelectField, 
                     TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY'] = 'pass123'

class InfoForm(FlaskForm):
    species = StringField('What species are you?', validators=[DataRequired()]) #creates an instance of DataRequired obj
    jedi = BooleanField('Do you have Jedi powers?')
    side = RadioField('Please choose your allegence:', choices=[('light','Light'), ('Dark','Dark')])
    weapon = SelectField(u'Please choose your favorite weapon': 
                         choices=[('saber','Light Saber'), ('blast','Blaster'),
                                  ('rifle','Sniper Rifle'),('turret','Turret Gun')]) #unicode mention to avoid OS specific errors
    feedback = TextAreaField()
    submit = SubmitField('Submit')

app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        # session is a data stored on server, time interval between when client is logged in/log out to set limit. stored temporarily 
        session['species'] = form.species.data
        session['jedi'] = form.jedi.data
        session['side'] = form.side.data
        session['weapon'] = form.weapon.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thank_you')) #redirects easily instead of messing with html for redirect
    return render_template('/forms_basic/form_fields_index.html', form=form)


app.route('/thank_you')
def thank_you():
    return render_template('/forms_basic/thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
