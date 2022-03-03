from os import environ
class Config:
	######################### Application Configurations #########################
		ENV = environ.get("TECHLAND_AUTHZ_FLASK_ENV", "production")
		SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
		DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_FLASK_DEBUG","0")))
		TESTING = DEBUG
		TIMEZONE = environ.get("TECHLAND_AUTHZ_TIMEZONE", "Asia/Tehran")
		
	######################### Database Configurations #########################		
		
		SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
		SQLALCHEMY_DATABASE_URI = environ.get("TECHLAND_AUTHZ_DATABASE_URI", None)
		SQLALCHEMY_ECHO = DEBUG	
		SQLALCHEMY_RECORD_QUERIES = DEBUG	
		
	######################### User Configurations #########################	

		USER_DEFAULT_ROLE =environ.get("TECHLAND_AUTHZ_USER_DEFAULT_ROLE", "member")
		USER_DEFAULT_EXPIRY_TIME = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365")) 
		USER_DEFAULT_STATUS = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_STATUS", "3"))
