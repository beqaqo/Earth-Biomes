from flask_admin import Admin
from flask_login import LoginManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

admin = Admin()
login_manager = LoginManager()
api = Api()
db = SQLAlchemy()
migrate = Migrate()