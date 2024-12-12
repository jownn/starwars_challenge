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


@patch("models.planet_model.mongo")
def test_get_all_planets(mock_mongo, client):
    mock_mongo.db.planets.find.return_value = [
        {
            "name": "Tatooine",
            "climate": "arid",
            "diameter": 10465,
            "population": 200000,
            "films": [ObjectId(), ObjectId(), ObjectId()],
        }
    ]
    response = client.get("/planets/")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Tatooine"


@patch("models.planet_model.mongo")
def test_get_planet(mock_mongo, client):
    mock_mongo.db.planets.find_one.return_value = {
        "name": "Tatooine",
        "climate": "arid",
        "diameter": 10465,
        "population": 200000,
        "films": [ObjectId(), ObjectId(), ObjectId()],
    }
    response = client.get("/planets/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Tatooine"


@patch("models.planet_model.mongo")
def test_add_planet(mock_mongo, client):
    mock_mongo.db.planets.insert_one.return_value.inserted_id = "1"
    payload = {
        "name": "Naboo",
        "climate": "temperate",
        "diameter": 12120,
        "population": 4500000000,
        "films": [ObjectId(), ObjectId()],
    }
    response = client.post("/planets/", json=json.loads(json.dumps(payload, default=str)))
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Planet added!"


@patch("models.planet_model.mongo")
def test_update_planet(mock_mongo, client):
    mock_mongo.db.planets.update_one.return_value.matched_count = 1
    payload = {
        "climate": "humid",
    }
    response = client.put("/planets/1", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Planet updated!"


@patch("models.planet_model.mongo")
def test_delete_planet(mock_mongo, client):
    mock_mongo.db.planets.delete_one.return_value.deleted_count = 1
    response = client.delete("/planets/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Planet deleted!"
