import json

from app.repositories.BusRepository import BusRepository


def test_create_bus(get_app, monkeypatch):
    dummy_data = {"id": 1, "capacity": 30, "model": "VW", "maker": "VW", "driver_id": 0}

    def mock_post(payload, session):
        return dummy_data

    monkeypatch.setattr(target=BusRepository, name="post", value=mock_post)

    response = get_app.post("/bus/", data=json.dumps({"capacity": 30, "model": "VW", "maker": "VW", "driver_id": 0}))
    assert response.status_code == 201
    assert response.json() == dummy_data


def test_create_bus_wrong_payload(get_app, monkeypatch):
    response = get_app.post("/bus/", data=json.dumps({"capacity": 10}))
    assert response.status_code == 422


def test_get_bus(get_app, monkeypatch):
    dummy_data = {"id": 1, "capacity": 30, "model": "VW", "maker": "VW", "driver_id": 0}

    def mock_get(id, session):
        return dummy_data

    monkeypatch.setattr(target=BusRepository, name="get", value=mock_get)

    response = get_app.get("/bus/1")
    assert response.status_code == 200
    assert response.json() == dummy_data


def test_get_bus_wrong_id(get_app, monkeypatch):
    def mock_get(id, session):
        return None

    monkeypatch.setattr(target=BusRepository, name="get", value=mock_get)

    response = get_app.get("/bus/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "Bus not found."
