from flask_restful import Resource
from authz.controller.apiv1 import UserController

class UserResource(Resource):

	def get(self, user_id=None):
		"""
		GET /users --> get list of users
		GET /user/<user_id> --> get user.
		"""
		if user_id is None:
			return UserController.get_users() # Get list of users
		else:
			return UserController.get_user(user_id) # Get user			
	
	def post(self):
		"""
		POST /users --> create nerw user.
		POST /user/<user_id> --> Not allowerd.
		"""
		return UserController.create_user() # Create new user
	
	def patch(self, user_id):
		"""
		PATCH /users --> Not allowed.
		PATCH /user/<user_id> --> Update user.
		"""
		return UserController.update_user(user_id) # Update user
	    
	def delete(self, user_id):
		"""
		DELETE /users --> Not allowed.
		DELETE /users/<user_id> --> Delete user.
		"""		
		return UserController.delete_user(user_id) # Delete user
	
