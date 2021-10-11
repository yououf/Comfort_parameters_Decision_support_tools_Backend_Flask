from flask import request, jsonify

import bcrypt

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from authentification import authentification_blueprint

from authentification.models import User


@authentification_blueprint.route("/login", methods=['POST'])
def check_credential():
    try:
        json_answer = request.get_json()

        pwd = json_answer.get('password')
        email = json_answer.get('email')

        if not pwd:
            return "There is no password", 400
        if not email:
            return "There is no email", 400

        user = User.query.filter_by(email=email).first()

        if not user:
            return "User not found", 404

        if bcrypt.checkpw(pwd.encode("utf-8"), user.password.encode("utf-8")):
            access_token = create_access_token(identity=user.serialize)
            refresh_token = create_refresh_token(identity=user.serialize)

            response = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            return jsonify(response), 200
        else:
            return "Wrong password", 404
    except AttributeError:
        return "No json found in the request"


@authentification_blueprint.route('/refresh', methods=['POST'])
#@jwt_refresh_token_required
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()

    access_token = create_access_token(identity=identity)

    response = {
        'access_token': access_token
    }
    return jsonify(response), 200
