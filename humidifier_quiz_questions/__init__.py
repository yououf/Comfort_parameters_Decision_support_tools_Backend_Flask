from flask import Blueprint

quiz_humidifier_questions_blueprint = Blueprint('quiz_humidifier_questions', __name__,
                                                url_prefix='/humidifiers/quiz_humidifier/questions/')

# import routes
from . import routes
