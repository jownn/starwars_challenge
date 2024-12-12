import json

import pytest
from unittest.mock import patch

from bson import ObjectId

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("models.movie_model.mongo")
def test_get_all_movies(mock_mongo, client):
    mock_mongo.db.movies.find.return_value = [
        {
            "title": "A New Hope",
            "release_date": "1977-05-25",
            "director": "George Lucas",
            "planets": [ObjectId(), ObjectId()],
        }
    ]
    response = client.get("/movies/")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "A New Hope"


@patch("models.movie_model.mongo")
def test_get_movie(mock_mongo, client):
    mock_mongo.db.movies.find_one.return_value = {
        "title": "A New Hope",
        "release_date": "1977-05-25",
        "director": "George Lucas",
        "planets": [ObjectId(), ObjectId()],
    }
    response = client.get("/movies/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "A New Hope"


@patch("models.movie_model.mongo")
def test_add_movie(mock_mongo, client):
    mock_mongo.db.movies.insert_one.return_value.inserted_id = "1"
    payload = {
        "title": "The Empire Strikes Back",
        "release_date": "1980-05-21",
        "director": "Irvin Kershner",
        "planets": [ObjectId(), ObjectId(), ObjectId()],
    }
    response = client.post("/movies/", json=json.loads(json.dumps(payload, default=str)))
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Movie added!"


@patch("models.movie_model.mongo")
def test_update_movie(mock_mongo, client):
    mock_mongo.db.movies.update_one.return_value.matched_count = 1
    payload = {
        "director": "Richard Marquand",
    }
    response = client.put("/movies/1", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Movie updated!"


@patch("models.movie_model.mongo")
def test_delete_movie(mock_mongo, client):
    mock_mongo.db.movies.delete_one.return_value.deleted_count = 1
    response = client.delete("/movies/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Movie deleted!"
