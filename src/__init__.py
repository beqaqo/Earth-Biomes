from flask_admin.menu import MenuLink
from flask_admin import Admin
from flask import Flask
from src.ext import admin, login_manager, api, db
from src.config import Config
from src.admin_views.base import SecureModelView
from src.admin_views.question import QuestionAdminView
from src.admin_views.biome import BiomeAdminView, BiomeInfoAdminView
from src.models import User, Biome, Question, BiomeInfo
from src.admin_views.base import SecureIndexView
from src.endpoints.biome import biome_ns
from src.endpoints.question import question_ns
from src.endpoints.biome import biome_ns
from src.endpoints.question import question_ns
from src.commands import register_commands
import src.endpoints.biome.biome
import src.endpoints.question.question


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    api.add_namespace(biome_ns)
    api.add_namespace(question_ns)

    api.init_app(app)
    admin.init_app(app, index_view=SecureIndexView())

    admin.add_view(BiomeAdminView(Biome, db.session, name='Biomes', endpoint='biomes_admin'))
    admin.add_view(BiomeInfoAdminView(BiomeInfo, db.session, name='Biome Infos', endpoint='biome_infos_admin'))
    admin.add_view(QuestionAdminView(Question, db.session, name='Questions', endpoint='questions_admin'))
    admin.add_link(MenuLink(name='Logout', url='/admin/logout/'))


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_commands(app)

    return app