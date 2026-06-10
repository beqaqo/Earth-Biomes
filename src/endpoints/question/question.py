from flask_restx import Resource
from src.models.question import Question
from src.endpoints.question import question_ns, question_model


@question_ns.route('/')
class QuestionApi(Resource):
    @question_ns.marshal_list_with(question_model)
    def get(self):
        return Question.query.all()