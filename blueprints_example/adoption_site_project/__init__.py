from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY123'

baseDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(baseDir,"puppy_adop.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
Migrate(app, db)

# db needs to be registered before so have to import blurprints after

from adoption_site_project.puppies.views import puppies_blueprints
from adoption_site_project.owners.views import owner_blueprints

app.register_blueprint(puppies_blueprints, url_prefix = '/puppies')
app.register_blueprint(owner_blueprints, url_prefix = '/owners')


