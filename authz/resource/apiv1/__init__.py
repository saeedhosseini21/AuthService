
from authz.authz import apiv1 as api
from authz.resource.apiv1.user import UserResource
from authz.resource.apiv1.auth import AuthResource

api.add_resource(
	UserResource,
	"/users",
	methods=["GET","POST"],
	endpoint="users"
 )

api.add_resource(
	UserResource,
	"/user/<user_id>",
	methods=["GET","PATCH","DELETE"],
	endpoint="user"
 )
 
api.add_resource(
	AuthResource,
	"/auth",
	methods=["GET","POST"],
	endpoint="auth"
 )


