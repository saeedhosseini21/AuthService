import pytest, json

# Creating users
@pytest.mark.parametrize(
  ("headers", "body", "status", "code"),
  [
	({}, {}, 415, 101),
	({"Content-Type": "application/json"}, {"username": 1, "password": 1}, 400, 104),
	({"Content-Type": "application/json"}, {"username": "test", "password": ""}, 400, 105),
	({"Content-Type": "application/json"}, {"username": "", "password": "test"}, 400, 105),
	({"Content-Type": "application/json"}, {"username": "test", "password": "test"}, 201, 100),
	({"Content-Type": "application/json"}, {"username": "test", "password": "test"}, 409, 106) # Duplicate user
  ]

)
def test_create_user(client, headers, body, status, code):
	result = client.post(
		"/api/v1/users",
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code



# Getting list of users
@pytest.mark.parametrize(
  ("headers", "status", "code"),
  [
	({"Content-Type": "application/json"}, 200, 100),
    ({}, 415, 101)
  ]

)
def test_get_users(client, headers, status, code):
	result = client.get(
		"/api/v1/users",
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code


# Getting a single user
@pytest.mark.parametrize(
  ("headers", "status", "code"),
  [
    ({}, 415, 101),
	({"Content-Type": "application/json"}, 200, 100)
  ]

)
def test_get_user(client, random_user, headers, status, code):
	result = client.get(
		f"/api/v1/user/{random_user.get('id')}",
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code



# Updating users
@pytest.mark.parametrize(
  ("headers", "body", "status", "code"),
  [
   	({}, {} , 415, 101),
 	({"Content-Type": "application/json"}, {"password": "" ,"oldpassword": "test", "dummyfield":"dummyvalue"} , 400, 104),
	({"Content-Type": "application/json"}, {"password": "" ,"oldpassword": "test"} , 400, 105),
	({"Content-Type": "application/json"}, {"password": "newtest", "oldpassword": "test"} , 200, 100)
  ]
)
def test_update_user(client, random_user, headers, body, status, code):
	result = client.patch(
		f"/api/v1/user/{random_user.get('id')}",
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code


# Deleting users
@pytest.mark.parametrize(
  ("headers", "status", "code"),
  [
 	({"Content-Type": "application/json"}, 200, 100)
  ]
)
def test_delete_user(client, random_user, headers, status, code):
	result = client.delete(
		f"/api/v1/user/{random_user.get('id')}",
		headers=headers
	)
	assert result.status_code == status
	assert result .get_json()["code"] == code
