from flask import jsonify, request
from app import mongo
from flask_api import status
from comfort_questions import comfort_feedback_questions_blueprint
from bson import ObjectId


@comfort_feedback_questions_blueprint.route("", methods=['GET'])
def get_feedback_questions():
    quiz_questions = mongo.db.questions_comfort
    output = [quiz_question for quiz_question in quiz_questions.find()]
    return jsonify(output)


@comfort_feedback_questions_blueprint.route("result", methods=['POST'])
def post_feedback_answers():
    if request.get_json() is None:
        return jsonify(
            error='Nothing in body'), status.HTTP_409_CONFLICT
    inserted_id = mongo.db.answers_comfort.insert_one(
        request.get_json()).inserted_id
    if inserted_id is None:
        return jsonify(
            error='Answer of the survey not saved'), \
               status.HTTP_409_CONFLICT
    return jsonify("Successfully created"), status.HTTP_201_CREATED
