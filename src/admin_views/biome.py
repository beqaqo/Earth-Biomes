import uuid
import os
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import ImageUploadField
from src.admin_views.base import SecureModelView
from wtforms import validators

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads')

def generate_unique_name(obj, file_data):
    ext = os.path.splitext(file_data.filename)[1]
    return f"{uuid.uuid4().hex}{ext}"

class BiomeAdminView(SecureModelView):

    column_list = ['name', 'location', 'previous_biome', 'next_biome']

    form_columns = [
        'name', 'location', 'climate', 'soil',
        'vegetation', 'important_plants',
        'previous_biome', 'next_biome',
        'biome_icon', 'title_img', 'distribution_img'
    ]

    form_extra_fields = {
        'biome_icon': ImageUploadField(
            'Biome Icon',
            base_path=UPLOAD_FOLDER,
            namegen=generate_unique_name,
            validators=[validators.DataRequired()]
        ),
        'title_img': ImageUploadField(
            'Title Image',
            base_path=UPLOAD_FOLDER,
            namegen=generate_unique_name,
            validators=[validators.DataRequired()]
        ),
        'distribution_img': ImageUploadField(
            'Distribution Image',
            base_path=UPLOAD_FOLDER,
            namegen=generate_unique_name,
            validators=[validators.DataRequired()]
        ),
    }