import pytest, json

# Creating jwt token
@pytest.mark.parametrize(
  ("headers", "body", "status", "code"),
  [
	({}, {}, 415, 101),
	({"Content-Type": "application/json"}, {"username": "test", "password": ""}, 400, 105),
	({"Content-Type": "application/json"}, {"username": "", "password": "testauth", "newpassword": "newtest"}, 400, 104),
	({"Content-Type": "application/json"}, {"username": "testauth", "password": "testauth"}, 401, 103),
  ]
)
def test_create_jwt_token(client, headers, body, status, code):
	result = client.post(
		"/api/v1/auth",
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code

# Validating jwt token
@pytest.mark.parametrize(
  ("headers", "status", "code"),
  [
	({}, 415, 101),
	({"Content-Type": "application/json", "X-Subject-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIU" },  500, 113)
  ]
)
def test_verify_jwt_token(client, headers, status, code):
	result = client.get(
		"/api/v1/auth",
		headers=headers
	)

	assert result.status_code == status
	assert result .get_json()["code"] == code
