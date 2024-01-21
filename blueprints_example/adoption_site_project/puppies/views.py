from flask import redirect, render_template, url_for
from adoption_site_project import db
from adoption_site_project.models import Puppy
from adoption_site_project.puppies.forms import AddForm, DelForm
from flask import Blueprint

puppies_blueprints = Blueprint('puppies', __name__,
                               template_folder='templates/puppies')


@puppies_blueprints.route('/add', methods = ['GET', 'POST'])
def add():
    print("Hello from puppies add")
    form = AddForm()
    
    #add to database and show list of puppies 
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        new_pup = Puppy(name, age)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    # add puppy default view
    return render_template("add.html", form = form)

@puppies_blueprints.route('/list')
def list():
 
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprints.route('/delete', methods= ['GET', 'POST'])
def delete():
    
    form = DelForm() 
    
    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        # pup = db.session.get(Puppy, form.id.data) why not this?
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("puppies.list"))
    
    return render_template('delete.html', form=form)