from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def administrator_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()

        if 'administrator' in identity['roles']:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='403 Forbidden'), 403

    return wrapper


def manager_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()

        if 'administrator' in identity['roles'] \
                or 'manager' in identity['roles']:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='403 Forbidden'), 403

    return wrapper
