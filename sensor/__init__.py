from flask import Blueprint

sensors_blueprint = Blueprint('sensors', __name__,
                              url_prefix='/sensors')

# import routes
from . import routes
