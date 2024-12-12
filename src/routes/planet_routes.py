from flask import Blueprint
from controllers.planet_controller import (
    get_all_planets,
    get_planet,
    add_planet,
    update_planet,
    delete_planet,
)

planet_blueprint = Blueprint("planets", __name__)

planet_blueprint.route("/", methods=["GET"])(get_all_planets)
planet_blueprint.route("/<planet_id>", methods=["GET"])(get_planet)
planet_blueprint.route("/", methods=["POST"])(add_planet)
planet_blueprint.route("/<planet_id>", methods=["PUT"])(update_planet)
planet_blueprint.route("/<planet_id>", methods=["DELETE"])(delete_planet)