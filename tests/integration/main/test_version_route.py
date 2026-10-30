"""
Test route for the app version, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument
import importlib

from app import create_app
from app import config


def create_client(monkeypatch, version):
    """
    Create a client for an app whose config is read with APP_VERSION set to version
    (or not set at all if version is None)
    """
    if version is None:
        monkeypatch.delenv("APP_VERSION", raising=False)
    else:
        monkeypatch.setenv("APP_VERSION", version)
    importlib.reload(config)
    return create_app(config.TestConfig).test_client()



def test_version_default(monkeypatch):
    """
    Without APP_VERSION the version is unknown
    """
    client = create_client(monkeypatch, None)
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"wrong"
    monkeypatch.undo()
    importlib.reload(config)



def test_version_set(monkeypatch):
    """
    The version comes from APP_VERSION, and no login is needed
    """
    client = create_client(monkeypatch, "11.0.1")
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"11.0.1"
    monkeypatch.undo()
    importlib.reload(config)
