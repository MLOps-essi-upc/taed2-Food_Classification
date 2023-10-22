from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from src.app.api import app

from PIL import Image

import json
import numpy as np


@pytest.fixture(scope="module", autouse=True)
def client():
    # Use the TestClient with a `with` statement to trigger the startup and shutdown events.
    with TestClient(app) as client:
        return client


@pytest.fixture
def payload():
    image = Image.open('data/test/beef_carpaccio/bc1.jpg')
    return json.dumps(np.array(image).tolist())
    

def test_root(client):
    response = client.get("/")
    json = response.json()
    assert response.status_code == 200
    assert (
        json["data"]["message"]
        == "Welcome to Food classifier! Please, read the `/docs`!"
    )
    assert json["message"] == "OK"
    assert json["status-code"] == 200
    assert json["method"] == "GET"
    assert json["url"] == "http://testserver/"
    assert json["timestamp"] is not None



def test_model_prediction(client, payload):
    response = client.post("/models", json=payload)
    json = response.json()
    assert response.status_code == 200
    assert json["data"]["predicted_class_id"] >= 0 and json["data"]["predicted_class_id"] <= 29
    assert json["message"] == "OK"
    assert json["status-code"] == 200
    assert json["method"] == "POST"
    assert json["url"] == "http://testserver/models"
    assert json["timestamp"] is not None