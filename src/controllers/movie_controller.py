
from flask import request
from models.movie_model import Movie
from models.movie_schema import MovieModel
from utils.utils import get_json_response


#TODO return the planet model together
def get_all_movies():
    movies = Movie.get_all()
    return get_json_response([movie.model_dump(by_alias=True) for movie in movies]), 200


def get_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return get_json_response({"error": "Movie not found"}), 404
    return get_json_response(movie.model_dump(by_alias=True)), 200


def add_movie():
    try:
        data = request.get_json()
        movie = MovieModel(**data)
        movie_id = Movie.add(movie.model_dump(by_alias=True))
        return get_json_response({"message": "Movie added!", "id": movie_id}), 201
    except Exception as e:
        print(e)
        return get_json_response({"error": str(e)}), 400


def update_movie(movie_id):
    try:
        data = request.get_json()
        updated_count = Movie.update(movie_id, data)
        if updated_count == 0:
            return get_json_response({"error": "Movie not found or not updated"}), 404
        return get_json_response({"message": "Movie updated!"}), 200
    except Exception as e:
        return get_json_response({"error": str(e)}), 400


def delete_movie(movie_id):
    deleted_count = Movie.delete(movie_id)
    if deleted_count == 0:
        return get_json_response({"error": "Movie not found"}), 404
    return get_json_response({"message": "Movie deleted!"}), 200
