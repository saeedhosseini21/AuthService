import pytest

from authz.authz import create_app

@pytest.fixture
def app():
	app = create_app()
	return app

@pytest.fixture
def client(app):
	return app.test_client()

@pytest.fixture
def random_user(client):
	result = client.get(
		"/api/v1/users",
		headers={"Content-Type": "application/json"}
	)
	return (result.get_json().get("users")[0]).get("id")
