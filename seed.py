from db import mongo
from app import create_app

app = create_app()

with app.app_context():
    planets = [
        {
            "name": "Tatooine",
            "climate": "arid",
            "diameter": "10465",
            "population": "200000",
             "movies": []
        },
        {
            "name": "Naboo",
            "climate": "temperate",
            "diameter": "12120",
            "population": "4500000000",
            "movies": []
        },
    ]

    movies = [
        {
            "title": "A New Hope",
            "release_date": "1977-05-25",
            "director": "George Lucas",
            "planets": []
        },
        {
            "title": "The Empire Strikes Back",
            "release_date": "1980-05-21",
            "director": "Irvin Kershner",
            "planets": []
        },
        {
            "title": "Return of the Jedi",
            "release_date": "1983-05-25",
            "director": "Richard Marquand",
            "planets": []
        },
    ]

    mongo.db.planets.delete_many({})
    mongo.db.movies.delete_many({})

    #TODO Update list with the objectId

    mongo.db.planets.insert_many(planets)
    mongo.db.movies.insert_many(movies)

    print("Banco de dados inicializado com sucesso!")