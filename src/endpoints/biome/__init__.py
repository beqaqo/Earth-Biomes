from flask_restx import Namespace, fields, reqparse

biome_ns = Namespace('biome', description='Biome operations')

image_model = biome_ns.model('Image', {
    'id': fields.Integer,
    'img': fields.String,
    'order': fields.Integer,
})

biome_info_model = biome_ns.model('BiomeInfo', {
    'id': fields.Integer,
    'category': fields.String,
    'description': fields.String,
    'images': fields.List(fields.Nested(image_model)),
})

# Full model - biome + biome_infos + images
biome_model = biome_ns.model('Biome', {
    'id': fields.Integer,
    'name': fields.String,
    'color': fields.String,
    'biome_icon': fields.String,
    'title_img': fields.String,
    'distribution_img': fields.String,
    'previous_biome': fields.Integer,
    'next_biome': fields.Integer,
    'biome_infos': fields.List(fields.Nested(biome_info_model)),
})

# Lite model - just what's left of the basic biome (no nested data)
biome_lite_model = biome_ns.model('BiomeLite', {
    'id': fields.Integer,
    'name': fields.String,
    'color': fields.String,
    'biome_icon': fields.String,
    'title_img': fields.String,
    'distribution_img': fields.String,
    'previous_biome': fields.Integer,
    'next_biome': fields.Integer,
})

biome_parser = reqparse.RequestParser()
biome_parser.add_argument('id', type=int, required=True, help='Biome ID is required')