from flask import Blueprint


pressure_blueprint = Blueprint('pressures', __name__,
                               url_prefix='/pressures/')

# import routes
from . import routes