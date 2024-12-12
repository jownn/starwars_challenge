from flask import request
from models.planet_model import Planet
from models.planet_schema import PlanetModel
from utils.utils import get_json_response

#TODO return the movie model together
def get_all_planets():
    planets = Planet.get_all()
    return get_json_response([PlanetModel(**planet).model_dump(by_alias=True) for planet in planets]), 200


def get_planet(planet_id):
    planet = Planet.get_by_id(planet_id)
    if not planet:
        return get_json_response({"error": "Planet not found"}), 404
    return get_json_response(PlanetModel(**planet).model_dump(by_alias=True)), 200


def add_planet():
    try:
        data = request.get_json()
        planet = PlanetModel(**data)
        planet_id = Planet.add(planet.model_dump(by_alias=True))
        return get_json_response({"message": "Planet added!", "id": planet_id}), 201
    except Exception as e:
        return get_json_response({"error": str(e)}), 400


def update_planet(planet_id):
    try:
        data = request.get_json()
        updated_count = Planet.update(planet_id, data)
        if updated_count == 0:
            return get_json_response({"error": "Planet not found or not updated"}), 404
        return get_json_response({"message": "Planet updated!"}), 200
    except Exception as e:
        return get_json_response({"error": str(e)}), 400


def delete_planet(planet_id):
    deleted_count = Planet.delete(planet_id)
    if deleted_count == 0:
        return get_json_response({"error": "Planet not found"}), 404
    return get_json_response({"message": "Planet deleted!"}), 200
