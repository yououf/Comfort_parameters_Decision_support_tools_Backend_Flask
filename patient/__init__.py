from flask import Blueprint

patients_blueprint = Blueprint('patients', __name__,
                               url_prefix='/patients/')

# import routes
from . import routes
