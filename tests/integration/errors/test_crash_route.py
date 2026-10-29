"""
Test the /crash route that is used to test monitoring, app/main/routes
"""
import pytest


def test_crash_raises(client):
    """
    The route raises. In testing mode Flask propagates the exception.
    """
    with pytest.raises(RuntimeError):
        client.get('/crash')


def test_crash_gives_500_page(client, test_app):
    """
    Without propagation the error handler answers with the 500 page.
    """
    test_app.config["PROPAGATE_EXCEPTIONS"] = False
    response = client.get('/crash')
    assert response.status_code == 500
    assert b"An unexpected error has occurred" in response.data
    assert b"Time of the error:" in response.data
