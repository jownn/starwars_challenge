from flask import Flask
from routes.planet_routes import planet_blueprint
from routes.movie_routes import movie_blueprint
from db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    init_db(app)

    app.register_blueprint(planet_blueprint, url_prefix="/planets")
    app.register_blueprint(movie_blueprint, url_prefix="/movies")

    return app