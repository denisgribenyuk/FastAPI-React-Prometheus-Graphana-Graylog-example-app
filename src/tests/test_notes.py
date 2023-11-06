import json
import pytest
from datetime import datetime as dt
from app.api import crud


def test_create_item(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else", "completed": False}
    test_response_payload = {
        "id": 1,
        "title": "something",
        "description": "something else",
        "completed": "False",
        "created_date": dt.now().strftime("%Y-%m-%d %H:%M"),
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/items/", data=json.dumps(test_request_payload))
    assert response.status_code == 201
    assert response.json() == test_response_payload
    
def test_create_item_invalid_json(test_app):
    response = test_app.post("/items/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422
    response = test_app.post("/items/", data=json.dumps({"title": "1", "description": "2"}))
    assert response.status_code == 422

# These tests should be run in order
def test_read_item(test_app, monkeypatch):
    test_data = {"id": 1, "title": "something", "description": "something else", 
    "completed": "False", "created_date": dt.now().strftime("%Y-%m-%d %H:%M")}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/items/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_item_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/items/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_read_item_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/items/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

    response = test_app.get("/items/0/")
    assert response.status_code == 422

#test for reading all items:
def test_read_all_items(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1, "completed": "True", "created_date": dt.now().strftime("%Y-%m-%d %H:%M")},
        {"title": "someone", "description": "someone else", "id": 2, "completed": "False", "created_date": dt.now().strftime("%Y-%m-%d %H:%M")},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/items/")
    assert response.status_code == 200
    assert response.json() == test_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar", "created_date": dt.now().strftime("%Y-%m-%d %H:%M"), "completed": "True"}, 404],
        [1, {"title": "1", "description": "bar"}, 422],
        [1, {"title": "foo", "description": "1"}, 422],
        [0, {"title": "foo", "description": "bar"}, 422],
    ],
)
def test_update_item_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/items/{id}/", data=json.dumps(payload),)
    assert response.status_code == status_code

#Test for DELETE route
def test_remove_item(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1, "completed": "False", "created_date": dt.now().strftime("%Y-%m-%d %H:%M")}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/items/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_item_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/items/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

    response = test_app.delete("/items/0/")
    assert response.status_code == 422
