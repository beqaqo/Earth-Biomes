from flask_restx import Namespace, fields

question_ns = Namespace('question', description='Question operations')

question_model = question_ns.model('Question', {
    'id': fields.Integer,
})

answer_model = question_ns.model('Answer', {
    'question_id': fields.Integer,
    'text': fields.String,
    'is_correct': fields.Boolean,
})

answer_input_model = question_ns.model('AnswerInput', {
    'question_id': fields.Integer(required=True),
    'answer': fields.String(required=True),
})