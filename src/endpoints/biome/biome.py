from flask_restx import Resource
from src.models.biome import Biome
from src.endpoints.biome import biome_ns, biome_model, biome_lite_model, biome_parser


@biome_ns.route('/')
class BiomeLiteApi(Resource):
    @biome_ns.marshal_list_with(biome_lite_model)
    def get(self):
        return Biome.query.all()


@biome_ns.route('/id')
class BiomeApi(Resource):
    @biome_ns.expect(biome_parser)
    @biome_ns.marshal_with(biome_model)
    def get(self):
        args = biome_parser.parse_args()
        return Biome.query.get_or_404(args['id'])