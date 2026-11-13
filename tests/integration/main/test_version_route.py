"""
Test the /version route, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument


def test_version_default(client):
    """
    Without APP_VERSION the version is unknown
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"unknown"



def test_version_set(client, test_app):
    """
    A set APP_VERSION is shown
    """
    test_app.config["APP_VERSION"] = "11.0.1"
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"11.0.1"
