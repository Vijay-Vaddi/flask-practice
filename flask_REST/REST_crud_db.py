from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from secure_check import login
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import get_jwt_identity, create_access_token
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'REST_test.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
Migrate(app, db)

api = Api(app)
jwt = JWTManager(app)

#####################################
class Puppy(db.Model):
    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name) -> None:
        self.name = name


    def json(self):
        return {'name': self.name}


#####################################


# puppies = []

class PuppyNames(Resource):

    def get(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        else:
            return {'name': None}, 404 # without 404 will give status 200 OK


    def post(self, name):
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()


    def put(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            pup.name = name 
            db.session.add(pup)
            db.session.commit()
            return pup.json()
        else:
            return {'Note':'Name not found'}


    def delete(self, name):
        pup = Puppy.query.filter_by(name=name).first()
        if pup: 
            db.session.delete(pup)
            return {'Note': 'Deteled successfully'}
        else:
            return {'name':'Not Found'}, 404

class AllPuppies(Resource):
    # @jwt_required()
    # will make the get api call to puppies needing auth
    def get(self):
        puppies = Puppy.query.all()
        if puppies:
            return [pup.json() for pup in puppies]
        else:
            return {'List' : None}, 404

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not username or not password:
            return jsonify({'msg':'username or password missing'})
        return login(username, password)
        
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllPuppies, '/puppies')
api.add_resource(UserLogin, '/login')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


