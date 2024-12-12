from flask import Blueprint
from controllers.movie_controller import (
    get_all_movies,
    get_movie,
    add_movie,
    update_movie,
    delete_movie,
)

movie_blueprint = Blueprint("movies", __name__)

movie_blueprint.route("/", methods=["GET"])(get_all_movies)
movie_blueprint.route("/<movie_id>", methods=["GET"])(get_movie)
movie_blueprint.route("/", methods=["POST"])(add_movie)
movie_blueprint.route("/<movie_id>", methods=["PUT"])(update_movie)
movie_blueprint.route("/<movie_id>", methods=["DELETE"])(delete_movie)

