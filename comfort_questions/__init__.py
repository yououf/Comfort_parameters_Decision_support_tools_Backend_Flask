from flask import Blueprint

comfort_feedback_questions_blueprint = Blueprint('comfort_feedback_questions', __name__,
                                                url_prefix='/comforts/feedback/')

# import routes
from . import routes
