# project/owners/views.py
from flask import render_template, redirect, url_for
from adoption_site_project import app, db
from adoption_site_project.models import Owner
from adoption_site_project.owners.forms import AddForm
from flask import Blueprint

owner_blueprint = Blueprint('owners', __name__, 
                            template_folder='templates/owners')

@owner_blueprint.route('/add', methods=['GET', 'POST'])
def add_owner():

    form = AddForm()

    if form.validate_on_submit():
        puppy_id = form.id.data
        name = form.name.data
        
        own = Owner(name, puppy_id)
        db.session.add(own)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    
    return render_template('add.html', form=form)




