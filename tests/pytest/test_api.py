from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from src.app.api import app

from PIL import Image

import json
import numpy as np
import os


@pytest.fixture(scope="module", autouse=True)
def client():
    # Use the TestClient with a `with` statement to trigger the startup and shutdown events.
    with TestClient(app) as client:
        return client



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



@pytest.mark.parametrize(
    "path", 
    [r"data/test/beef_carpaccio/bc4.jpg",
    r"data/test/food_test_1/0.jpg",
    r"data/test/food_test_1/7.jpg"
    ]
)

def test_prediction(client, path):  
    # Use constants if fixture created
    with open(path, "rb") as image_file:
        files = {"file": ("test_image.jpg", image_file, "image/jpeg")}
        print(files)
        response = client.post("/models", files=files)
    json = response.json()
    assert response.status_code == 200
    assert json["data"]["predicted_class_id"] >= 0 and json["data"]["predicted_class_id"] <= 29
    assert json["message"] == "OK"
    assert json["status-code"] == 200
    assert json["method"] == "POST"
    assert json["url"] == "http://testserver/models"
    assert json["timestamp"] is not None