"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required
from flask import Flask, request, jsonify, url_for, Blueprint, make_response
from api.utils import generate_sitemap, APIException
import uuid
from  werkzeug.security import generate_password_hash, check_password_hash


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def login ():
    try: 
        data = request.json
        print(data)
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({"data": "user not found" , "code" :0})
        else: 
            print(user)
            if user.password == password:
                access_token= create_access_token(identity=user.id)
                return jsonify({"code": 1, "token": access_token})
            else:
                return jsonify({"code": 2, "response": "email or password is incorrect"})
    except Exception as e: 
        print(e)

@api.route('/signup', methods=['POST'])
def signup():
    try:
     #objeto json
        data = request.json
        #gets email and password
        email = data["email"]
        #checking for existing user
        user = User.query.filter_by(email = email).first()
        
        if   user is None:
            newUser = User(
            name = data["name"],
            email = data["email"], 
            password = data["password"]
            )
            print(newUser)
        #insert users
            db.session.add(newUser)
            db.session.commit()
            #return make_response("Done", 200) 
            response = jsonify({"response": "Se creo usuario exitosamente", "status" : 200, "code" : 0})
            response.headers.add('Access-Control-Allow-Origin', '*') 
            return response


        return jsonify({"response" :"usuario ya existe", "status" : 200, "code" : 1})

    except Exception as e:
     print(e)
     return jsonify({"response": "Error", "status" : 500, "code" : e})
     

        




