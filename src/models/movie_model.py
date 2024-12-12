from db import mongo
from models.movie_schema import MovieModel
from datetime import datetime


class Movie:
    @staticmethod
    def get_all():
        movies = list(mongo.db.movies.find())
        return [MovieModel(**movie) for movie in movies]

    @staticmethod
    def get_by_id(movie_id):
        movie = mongo.db.movies.find_one({"_id": movie_id})
        if not movie:
            return None
        return MovieModel(**movie)

    @staticmethod
    def add(data):
        result = mongo.db.movies.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def update(movie_id, data):
        data["updated_at"] = datetime.utcnow()
        result = mongo.db.movies.update_one(
            {"_id": movie_id}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    def delete(movie_id):
        result = mongo.db.movies.delete_one({"_id": movie_id})
        return result.deleted_count
