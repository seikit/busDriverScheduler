from datetime import date

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def get_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="session")
def dummy_payload():
    return {
        "id": 1,
        "bus_id": 1,
        "driver_id": 1,
        "shift": str(date.today())
    }
