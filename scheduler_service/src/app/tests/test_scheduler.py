import json
from datetime import date

from app.repositories.ScheduleRepository import ScheduleRepository


def test_create_schedule(get_app, dummy_payload, monkeypatch):

    def mock_post(self, payload):
        return dummy_payload

    monkeypatch.setattr(target=ScheduleRepository, name="post", value=mock_post)

    response = get_app.post("/schedule/", data=json.dumps({
        "bus_id": 1,
        "driver_id": 1,
        "shift": str(date.today())
    }))
    assert response.status_code == 201
    assert response.json() == dummy_payload


def test_create_schedule_wrong_payload(get_app, monkeypatch):
    response = get_app.post("/schedule/", data=json.dumps({"shift": 10}))
    assert response.status_code == 422


def test_get_schedule(get_app, dummy_payload, monkeypatch):
    def mock_get(self, id):
        return dummy_payload

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)

    response = get_app.get("/schedule/1")
    assert response.status_code == 200
    assert response.json() == dummy_payload


def test_get_schedule_wrong_id(get_app, monkeypatch):
    def mock_get(self, id):
        return None

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)

    response = get_app.get("/schedule/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "Schedule not found."


def test_update_schedule(get_app, dummy_payload, monkeypatch):
    updated_schedule = {
        "id": 1,
        "bus_id": 2,
        "driver_id": 2,
        "shift": str(date.today())
    }

    def mock_get(self, id):
        return dummy_payload

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)

    def mock_update(self, schedule_model, payload):
        return updated_schedule

    monkeypatch.setattr(target=ScheduleRepository, name="update", value=mock_update)

    response = get_app.put("/schedule/1/", data=json.dumps(dummy_payload))
    assert response.status_code == 200
    assert response.json() == updated_schedule


def test_update_schedule_w_wrong_id(get_app, dummy_payload, monkeypatch):
    def mock_get(self, id):
        return None

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)

    response = get_app.put("/bus/1000/", data=json.dumps(dummy_payload))
    assert response.status_code == 404


def test_delete_schedule(get_app, dummy_payload, monkeypatch):
    def mock_get(self, id):
        return dummy_payload

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)

    def mock_delete(self, schedule_model):
        return None

    monkeypatch.setattr(target=ScheduleRepository, name="delete", value=mock_delete)

    response = get_app.delete("/schedule/1/")
    assert response.status_code == 200


def test_delete_schedule_wrong_id(get_app, monkeypatch):
    def mock_get(self, id):
        return None

    monkeypatch.setattr(target=ScheduleRepository, name="get", value=mock_get)
    response = get_app.delete("/bus/2/")
    assert response.status_code == 404

