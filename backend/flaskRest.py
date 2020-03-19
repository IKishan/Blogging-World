# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello flask restful'})
    
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201

class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})

class Register(Resource):
    def get(self):
        return jsonify({'register': "UP and RUNNING!!"})
    
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Register, '/register')

if __name__ == "__main__":
    app.run(debug = True)