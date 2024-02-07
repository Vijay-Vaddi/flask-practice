from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Hello(Resource):

    def get(self):
        return {'hello': 'World'}

api.add_resource(Hello, '/')

if __name__ == "__main__":
    app.run(debug=True)

