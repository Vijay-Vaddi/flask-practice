from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_login123'
app.config['MESSAGE_FLASHING_OPTIONS'] = {'duration': 3}

login_manager = LoginManager()
# LoginManager class effectively automate all the management of login systems
 
baseDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(baseDir, 'login_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
Migrate(app, db)

login_manager.init_app(app)
# configs app to have management of login users
login_manager.login_view = "login"
# what view to go to when user hits login, written in views
