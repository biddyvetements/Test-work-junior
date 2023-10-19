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
        list_questions_api = get_questions(args['questions_num'])
        session = create_session()

        all_questions_db = session.query(Question.id).all()

        list_questions_api.append({
            "id": 2848,
            "answer": "counterclockwise",
            "question": "In the Northern Hemisphere, hurricane winds blow around the storm's eye in this direction",
            "value": 300,
            "airdate": "1986-02-06T20:00:00.000Z",
            "created_at": "2022-12-30T18:38:46.514Z",
            "updated_at": "2022-12-30T18:38:46.514Z",
            "category_id": 457,
            "game_id": 2263,
            "invalid_count": None,
            "category": {
                "id": 457,
                "title": "storms",
                "created_at": "2022-12-30T18:38:46.447Z",
                "updated_at": "2022-12-30T18:38:46.447Z",
                "clues_count": 8
            }
        })
        latest_question = None
        list_to_add = []
        for question_item in list_questions_api:
            if ((question_item['id'],) not in all_questions_db):
                new_question = Question(id=question_item['id'], question_text=question_item['question'],
                                        answer_text=question_item['answer'], created_at=question_item['created_at'])
                list_to_add.append(new_question)
                latest_question = question_item

        session.add_all(list_to_add)
        session.commit()
        session.close()
        return {'success': True, 'latest_question': latest_question}, 200


# 1.176398833999997

api.add_resource(InsertQuestions, '/api/questions/')

if __name__ == '__main__':
    global_init('postgresql://baeldung:baeldung@212.193.51.197/baeldung')
    app.run(debug=True, host='127.0.0.1', port=os.environ.get('port', '3000'))
