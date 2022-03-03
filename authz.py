from flask import FLASK, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from authz.config import config

db = SQLAlchemy()

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix='/api/v1')
apiv1 = Api(apiv1_bp)

def create_app(config_filename):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object()
    return app
  
