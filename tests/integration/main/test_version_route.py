"""
Test the /version route in app/main/routes
"""
# pylint: disable=redefined-outer-name
import importlib
import pytest
from app import create_app
import app.config



@pytest.fixture
def version_client(monkeypatch, request):
    """
    Create a test client where APP_VERSION is set to request.param, or unset if None.
    The config is read when app/config.py is imported, so it is reloaded here.
    """
    if request.param is None:
        monkeypatch.delenv("APP_VERSION", raising=False)
    else:
        monkeypatch.setenv("APP_VERSION", request.param)
    config = importlib.reload(app.config)
    test_app = create_app(config.TestConfig)
    return test_app.test_client()



@pytest.mark.parametrize("version_client", [None], indirect=True)
def test_version_default(version_client):
    """
    Without APP_VERSION the route answers unknown, and no login is needed
    """
    response = version_client.get("/version")
    assert response.status_code == 200
    assert response.data == b"unknown"



@pytest.mark.parametrize("version_client", ["11.0.1"], indirect=True)
def test_version_set(version_client):
    """
    With APP_VERSION set the route answers with it
    """
    response = version_client.get("/version")
    assert response.status_code == 200
    assert response.data == b"11.0.1"
    assert response.mimetype == "text/plain"
