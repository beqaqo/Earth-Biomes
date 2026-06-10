from flask_restx import Namespace, fields

question_ns = Namespace('question', description='Question operations')

question_model = question_ns.model('Question', {
    'id': fields.Integer,
    'a': fields.String,
    'b': fields.String,
    'c': fields.String,
    'd': fields.String,
    'correct': fields.String,
})