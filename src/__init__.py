from flask_admin.menu import MenuLink
from flask_admin import Admin
from flask import Flask
from src.ext import admin, login_manager, api, db
from src.config import Config
from src.models import User, Biome, Question
from src.admin_views.base import SecureModelView
from src.admin_views.biome import BiomeAdminView
from src.admin_views.question import QuestionAdminView
from src.models import User
from src.admin_views.base import SecureIndexView


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    api.init_app(app)
    admin.init_app(app, index_view=SecureIndexView())

    admin.add_view(BiomeAdminView(Biome, db.session, name='Biomes'))
    admin.add_view(QuestionAdminView(Question, db.session, name='Questions'))
    admin.add_link(MenuLink(name='Logout', url='/admin/logout/'))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app