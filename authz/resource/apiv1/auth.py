from flask_restful import Resource 
from authz.controller.apiv1 import AuthController

class AuthResource(Resource):

	def get(self):
		"""
		GET /auth.tokens --> Verify the token
		"""
		return AuthController.verify_jwt_token() # Verify the token
	
	def post(self):
		"""
		POST /auth/tokens --> Generate a new token
		"""
		return AuthController.create_jwt_token() # Generate a new token
