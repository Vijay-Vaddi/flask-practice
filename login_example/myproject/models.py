from myproject import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
#usermixin has loggin in users and authorizing 

# going to allow flask login to load the current user and grab their ID
# used to show someone pages specific to their id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True)
    user_name = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, user_name, password):
        self.email = email
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    