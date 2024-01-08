from flask import Flask, render_template, url_for, flash, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MYKEY'

class SimpleForm(FlaskForm):
    breed = StringField('Enter your breed and hit submit')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():

    form = SimpleForm()
    
    if form.validate_on_submit():
        session ['breed'] = form.breed.data
        flash(f"You've entered the breed : {session['breed']} ") #can do .format() as well. 
        return redirect(url_for('index'))

    return render_template('./forms_basic/flash_example.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


