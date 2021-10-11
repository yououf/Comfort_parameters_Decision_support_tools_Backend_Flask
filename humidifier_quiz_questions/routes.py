from flask import jsonify, request
from app import mongo
from flask_api import status
from humidifier_quiz_questions import quiz_humidifier_questions_blueprint
from bson import ObjectId


@quiz_humidifier_questions_blueprint.route("", methods=['GET'])
def get_quiz_questions():
    quiz_questions = mongo.db.questions_humidifier
    output = []
    for quiz_question in quiz_questions.find():
        output.append(quiz_question)
    return jsonify(output)


@quiz_humidifier_questions_blueprint.route("result", methods=['POST'])
def post_quiz_answers():
    if request.get_json() is None:
        return jsonify(
            error='Nothing in body'), status.HTTP_409_CONFLICT
    inserted_id = mongo.db.answers_humidifier.insert_one(
        request.get_json()).inserted_id
    if inserted_id is None:
        return jsonify(
            error='Answer of the survey not saved'), \
               status.HTTP_409_CONFLICT
    return jsonify("Successfully created"), status.HTTP_201_CREATED
