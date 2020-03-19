from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import userService

app = Flask(__name__) 
api = Api(app)
CORS(app)

class Register(Resource):

    def get(self):
        return jsonify({"message": "Register API - GET method"})

    def post(self):
        formData = request.get_json()
        # print("FORM DATA --> ", formData)
        # print(formData['name'])
        res = make_response(jsonify(userService.createUser(formData)), 201)
        return res

class Login(Resource):

    def get(self):
        return jsonify({"message": "Login API - GET method"})
    
    def post(self):
        loginData = request.get_json()
        # print("LOGIN DATA --> ", loginData)
        # print(loginData['username'])
        res = make_response(jsonify(userService.loginUser(loginData)), 201)
        return res

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

if __name__ == '__main__': 
	app.run(debug = True)
