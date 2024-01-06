from flask import Flask, render_template
from flask_wtf import FlaskForm
#flaskForm is a class we're going to inherit from to create our own forms. 
from wtforms import StringField, SubmitField
#importing fields that are going in our custom form. 

app = Flask(__name__)

# configure secret key for CSRF security to work. 
#learn more on this. 

app.config['SECRET_KEY'] = 'secretpass123'
#grab our app, then grab config dictionary, secret_key is key thats built into our flask app configuration. 
# much better to set it an environment variable incase someone sees our .py script

#now we've to create an instance of WTF forms with our custom fields
#and then create a view function that creates an instance of that class and checks if its a valid submission

class InfoForm(FlaskForm): #custom class name of our form, inheriting Flaskform
    
    breed = StringField('What breed are you') #inside is label for field
    submit = SubmitField('Submit')

#our view function
@app.route('/', methods =['GET', 'POST'] )
def index():
    breed = False

    form = InfoForm()

    if form.validate_on_submit(): #check if all validators are met
        breed = form.breed.data #grab the data and set data to '' for later, then pass to html
        form.breed.data = ''
    
    return render_template('/forms_basic/basic_form.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)