import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def get_app():
    client = TestClient(app)
    yield client
