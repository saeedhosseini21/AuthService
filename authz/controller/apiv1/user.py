from flask import request
from authz.util.jsonify import jsonify
from authz.authz import db
from authz.model import User
from authz.schema.apiv1 import UserSchema

class UserController:
	def get_users():
		if request.content_type != "application/json":
			return jsonify (status=415, code=101) # Invalid Media Type
		try:
			users = User.query.all()
		except Exception as e:
			return jsonify(status=500,code=102) # Database error.
		users_schema = UserSchema(many=True)
		return jsonify({
			"users": users_schema.dump(users)}
		)

	def get_user(user_id):
		if request.content_type != "application/json":
			return jsonify (status=415, code=101) # Database error.
		user_schema = UserSchema()
		try:
			user = User.query.filter_by(id=user_id).first()
			print(user_id)
		except Exception as e:
			return jsonify(status=500,code=102) # Database error.
		return jsonify(
			{"user": user_schema.dump(user)}
		)			
			
	def create_user():
		if request.content_type != "application/json":
			return jsonify(status=415, code=101)
		user_schema = UserSchema(only=["username","password"])
		try:
			user_data = user_schema.load(request.get_json()) # Read and validate user data.
		except Exception as e:
			return jsonify(status=400, code=104)
			
		if not user_data.get("username") or not user_data.get("password"):
			return jsonify(status=400, code=105) # Empty Data
		try:	
			user = User.query.filter_by(username=user_data.get("username")).first()
		except Exception as e:
			return jsonify(status=500,code=102) # Database error.		
		if user is not None:
			return jsonify(status=409,code=106) # user already exists
		user = User(
			username=user_data.get("username"),
			password=user_data.get("password")
		)
		db.session.add(user)
		try:
			db.session.commit() # Execute insert command.
		except Exception as e:
			db.session.rollback()	
			return jsonify(status=500,code=102) # Database error.	
		user_schema = UserSchema()
		return jsonify(
			{"user": user_schema.dump(user) }, status=201
		)		
		
			
	 
	def update_user(user_id):
		if request.content_type != "application/json":
			return jsonify (status=415, code=101)
		user_schema = UserSchema(only=["username","password"])
		try:
			user_data = user_schema.load(request.get_json())
		except Exception as e:
			return jsonify(status=400, code=104)
		if not user_data.get("username") or not user_data.get("password"):
			return jsonify(status=400, code=105) # Empty Data
		if not User.query.filter_by(id=user_id):
			pass
		pass
		#todo: this must be done just by Admin.
				
			
		
			
	def delete_user(user_id):
		return jsonify(status=501, code=107) #Not Implemented
