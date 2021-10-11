from flask import Blueprint
from . import models

authentification_blueprint = Blueprint('authentification', __name__,
                               url_prefix='/authentification/')

# import routes
from . import routes