from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from secure_check import login
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import get_jwt_identity, create_access_token

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

api = Api(app)
# jwt = JWT(app,authenticate,identity)
jwt = JWTManager(app)

puppies = []

class Puppy(Resource):

    def get(self, name):
        for pup in puppies:
            if name == pup['name']:
                return pup
        return {'name': None}, 404 # without 404 will give status 200 OK


    def post(self, name):
        pup = {'name':name}
        puppies.append(pup)

        return pup


    def put(self, name):
        for ind, pup in enumerate(puppies):
            if name == pup['name']:
                puppies[ind] = {'name':name}
                return puppies[ind]
        return {'Note':'Name not found'}


    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if name == pup['name']:
                puppies.pop(ind)
                return {'Note': 'Deteled successfully'}
        
        return {'name':'Not Found'}

class AllPuppies(Resource):
    @jwt_required()
    # will make the get api call to puppies needing auth
    def get(self):
        current_user = get_jwt_identity()
        if current_user:
            return {'Puppies': puppies}

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not username or not password:
            return jsonify({'msg':'username or password missing'})
        return login(username, password)
        
api.add_resource(Puppy, '/puppy/<string:name>')
api.add_resource(AllPuppies, '/puppies')
api.add_resource(UserLogin, '/login')

if __name__ == "__main__":
    app.run(debug=True)


