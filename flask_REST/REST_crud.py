from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

puppies = []

class Puppy(Resource):

    def get(self, name):

        for pup in puppies:
            if name == pup['name']:
                return pup
        return {'name': None}


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
    def get(self):
        return {'Puppies': puppies}

api.add_resource(Puppy, '/puppy/<string:name>')
api.add_resource(AllPuppies, '/puppies')

if __name__ == "__main__":
    app.run(debug=True)


