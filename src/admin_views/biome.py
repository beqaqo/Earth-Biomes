import uuid
import os
from flask_admin.form import ImageUploadField
from flask_admin.model.form import InlineFormAdmin
from .base import SecureModelView
from wtforms import validators, SelectField
from src.models.image import Image

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads')

CATEGORY_CHOICES = [
    ('location', 'Location'),
    ('climate', 'Climate'),
    ('soil', 'Soil'),
    ('vegetation_structure', 'Vegetation Structure'),
    ('vegetation', 'Vegetation'),
    ('important_plants', 'Important Plants'),
]


def generate_unique_name(obj, file_data):
    ext = os.path.splitext(file_data.filename)[1]
    return f"{uuid.uuid4().hex}{ext}"


class BiomeAdminView(SecureModelView):

    column_list = ['name', 'previous_biome', 'next_biome']

    form_columns = [
        'name', 'color',
        'previous_biome', 'next_biome',
        'biome_icon', 'title_img', 'distribution_img',
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


class ImageInlineModel(InlineFormAdmin):
    form_columns = ['id', 'img', 'order']

    form_extra_fields = {
        'img': ImageUploadField(
            'Image',
            base_path=UPLOAD_FOLDER,
            namegen=generate_unique_name,
        )
    }

    def __init__(self):
        super().__init__(Image)


class BiomeInfoAdminView(SecureModelView):
    column_list = ['category', 'biome']

    form_columns = ['category', 'description', 'biome']

    form_extra_fields = {
        'category': SelectField(choices=CATEGORY_CHOICES, validators=[validators.DataRequired()])
    }

    inline_models = (ImageInlineModel(),)