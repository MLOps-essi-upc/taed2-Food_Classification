from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from src.app.api import app


@pytest.fixture(scope="module", autouse=True)
def client():
    # Use the TestClient with a `with` statement to trigger the startup and shutdown events.
    with TestClient(app) as client:
        return client


@pytest.fixture
def payload():
    return {
        "sepal_length": 6.4,
        "sepal_width": 2.8,
        "petal_length": 5.6,
        "petal_width": 2.1,
    }


def test_root(client):
    response = client.get("/")
    json = response.json()
    assert response.status_code == 200
    assert (
        json["data"]["message"]
        == "Welcome to Food classifier! Please, read the `/docs`!!"
    )
    assert json["message"] == "OK"
    assert json["status-code"] == 200
    assert json["method"] == "GET"
    assert json["url"] == "http://0.0.0.0:8000/"
    assert json["timestamp"] is not None



def test_model_prediction(client, payload):
    response = client.post("/models/LogisticRegression", json=payload)
    json = response.json()
    assert response.status_code == 200
    assert json["data"]["prediction"] == 2
    assert json["message"] == "OK"
    assert json["status-code"] == 200
    assert json["method"] == "POST"
    assert json["url"] == "http://testserver/models/LogisticRegression"
    assert json["timestamp"] is not None