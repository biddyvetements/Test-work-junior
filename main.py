import os
import time
from sqlalchemy.exc import IntegrityError
import requests
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from db import create_session, global_init, Question

app = Flask(__name__)
api = Api(app)


def get_questions(quantity: int):
    params = {
        'count': quantity,
    }

    response = requests.get('https://jservice.io/api/random', params=params)
    return response.json()


class InsertQuestions(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('questions_num', help='This field is required', required=True)
        args = parser.parse_args()
        list_questions = get_questions(args['questions_num'])
        session = create_session()

        all_questions = session.query(Question.id).all()
        latest_question = None
        list_to_add = []
        for question_item in list_questions:
            if (question_item['id'] not in all_questions):
                new_question = Question(id=question_item['id'], question_text=question_item['question'],
                                        answer_text=question_item['answer'], created_at=question_item['created_at'])
                list_to_add.append(new_question)
                latest_question = question_item

        session.add_all(list_to_add)
        session.close()
        return {'success': True, 'latest_question': latest_question}, 200


# 1.176398833999997

api.add_resource(InsertQuestions, '/api/questions/')

if __name__ == '__main__':
    global_init('postgresql://baeldung:baeldung@212.193.51.197/baeldung')
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('port', '3000'))
