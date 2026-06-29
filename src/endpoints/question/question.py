from flask_restx import Resource
from flask import request
from src.models.question import Question
from src.endpoints.question import question_ns, question_model, answer_model, answer_input_model


@question_ns.route('/')
class QuestionApi(Resource):
    @question_ns.marshal_list_with(question_model)
    def get(self):
        return Question.query.all()

    @question_ns.expect(answer_input_model)
    @question_ns.marshal_list_with(answer_model)
    def post(self):
        data = request.get_json()
        answers = []
        for question in data:
            question_id = question.get('question_id')
            question = Question.query.get_or_404(question_id)

            answers.append([
                {'question_id': question.id, 'text': question.a, 'is_correct': question.correct == 'a'},
                {'question_id': question.id, 'text': question.b, 'is_correct': question.correct == 'b'},
                {'question_id': question.id, 'text': question.c, 'is_correct': question.correct == 'c'},
                {'question_id': question.id, 'text': question.d, 'is_correct': question.correct == 'd'},
            ])

        return answers