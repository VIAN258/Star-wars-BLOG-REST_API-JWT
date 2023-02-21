"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required


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
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({"data": "user not found" , "code" :0})
        else: 
            if user.password == password:
                access_token= create_access_token(identity=user.id)
                return jsonify({"code": 1})
            else:
                return jsonify({"code": 2, "data": "email or password is incorrect"})
    except Exception as e: 
        print(e)


@api.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        name = data ["name"]
        email = data["email"]
        password = data["password"]
        print(data)
        user = db.User.query.filter_by(email=email).first()
        if user is None:
           print("fel")
           newUser= User(name, email, password)
           db.session.add(newUser)
           db.session.commit()
           response=jsonify(data="create", status=200, code = 3)
           response.headers.add("Access-Control-Allow-Origin" , "*")
           return response
        else:
            return jsonify({"code": 4, "data": "user exist"})
    except Exception as e:
        print(e)





