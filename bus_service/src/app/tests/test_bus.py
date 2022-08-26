import json

from app.repositories.BusRepository import BusRepository


def test_create_bus(get_app, monkeypatch):
    dummy_data = {"id": 1, "capacity": 30, "model": "VW", "maker": "VW", "driver_id": 0}

    def mock_post(payload, session):
        return dummy_data

    monkeypatch.setattr(target=BusRepository, name="post", value=mock_post)

    response = get_app.post("/bus/", data=json.dumps(dummy_data))
    assert response.status_code == 201
    assert response.json() == dummy_data
