from os import environ

######################### Application Configurations #########################

ENV = environ.get("TECHLAND_AUTHZ_FLASK_ENV", "production")
SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_FLASK_DEBUG"), "0"))
TESTING = DEBUG

