from flask_restx import Namespace, fields, reqparse

biome_ns = Namespace('biome', description='Biome operations')

# Full model - all fields
biome_model = biome_ns.model('Biome', {
    'id': fields.Integer,
    'name': fields.String,
    'location': fields.String,
    'climate': fields.String,
    'soil': fields.String,
    'vegetation': fields.String,
    'important_plants': fields.String,
    'biome_icon': fields.String,
    'title_img': fields.String,
    'distribution_img': fields.String,
    'previous_biome': fields.Integer,
    'next_biome': fields.Integer,
})

# Lite model - only name
biome_lite_model = biome_ns.model('BiomeLite', {
    'id': fields.Integer,
    'name': fields.String,
})

# Parser - accepts id to fetch specific biome
biome_parser = reqparse.RequestParser()
biome_parser.add_argument('id', type=int, required=True, help='Biome ID is required')