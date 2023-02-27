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




# --------------GET-----------------------

@app.route('/character', methods=['GET'])
def get_character():
    allcharacter = Character.query.all()
    results = list(map(lambda item: item.serialize(),allcharacter))

    return jsonify(results), 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_id(character_id):

    character = Character.query.filter_by(id=character_id).first()
    return jsonify(character.serialize()), 200


@app.route('/planet', methods=['GET'])
def get_planet():

    allplanet = Planet.query.all()
    results = list(map(lambda item: item.serialize(),allplanet))

    return jsonify(results), 200


@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_id(planet_id):

    planet = Planet.query.filter_by(id=planet_id).first()
    return jsonify(planet.serialize()), 200

@app.route('/user', methods=['GET'])
def get_user():

    allusers = User.query.all()
    results = list(map(lambda item: item.serialize(),allusers))

    return jsonify(results), 200

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):

    favs = Favorites.query.filter_by(user_id=user_id).all()
    results = list(map(lambda item: item.serialize(),favs))

    return jsonify(results), 200


# --------------POST-----------------------

@app.route('/user/<int:user_id>/favorites/planets', methods=['POST'])
def add_planet_favorites(user_id):

    request_body = request.json
    print(request_body)
    print(request_body['planets_id'])
    new_fav_planet = Favorites(user_id = user_id, character_id = None, ship_id = None, planet_id = request_body['planet_id']) 
    favs = Favorites.query.filter_by(user_id=user_id, planet_id=request_body['planet_id']).first()
    print(favs)
    if favs is None:
        new_fav_planet = Favorites(user_id = user_id, character_id = None, ship_id = None, planet_id = request_body['planet_id']) 
        db.session.add(new_fav_planet)
        db.session.commit()

        return jsonify({new_fav_planet}), 200    

    return jsonify({'msg': 'el favorito ya existe'}), 400


@app.route('/user/<int:user_id>/favorites/character', methods=['POST'])
def add_people_favorites(user_id):

    request_body = request.json
    print(request_body)
    print(request_body['character_id'])
    new_fav_people = Favorites(user_id = user_id, character_id = request_body['character_id'], ship_id = None, planet_id = None) 
    favs = Favorites.query.filter_by(user_id=user_id, charcater_id=request_body['character_id']).first()
    print(favs)
    if favs is None:
        new_fav_people = Favorites(user_id = user_id, charcater_id = request_body['character_id'], ship_id = None, planet_id = None) 
        db.session.add(new_fav_people)
        db.session.commit()

        return jsonify({new_fav_people}), 200    

    return jsonify({'msg': 'el favorito ya existe'}), 400


# --------------DELETE-----------------------

@app.route('/user/<int:user_id>/favorites/planet', methods=['DELETE'])
def delete_planet_favorites(user_id):

    request_body = request.json
    print(request_body)
    print(request_body['planet_id'])
    favs = Favorites.query.filter_by(user_id=user_id, planet_id=request_body['planet_id']).first()
    print(favs)

    if favs is not None:
        db.session.delete(favs)
        db.session.commit()

        return jsonify({'msg': 'eliminaste el favorito correctamente'}), 200    

    return jsonify({'msg': 'No existe el favorito a eliminar'}), 400

@app.route('/user/<int:user_id>/favorites/people', methods=['DELETE'])
def delete_people_favorites(user_id):

    
    request_body = request.json
    print(request_body)
    print(request_body['character_id'])
    favs = Favorites.query.filter_by(user_id=user_id, charcater_id=request_body['character_id']).first()
    print(favs)
    if favs is not None:
        db.session.commit()
        db.session.commit()
        
        return jsonify({'msg': 'eliminaste el favorito correctamente'}), 200    

    return jsonify({'msg': 'No existe el favorito a eliminar'}), 400

     

        




