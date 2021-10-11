from flask import Blueprint

environmental_data_blueprint = Blueprint('environmental_data', __name__,
                                         url_prefix='/environmental_data')

# import routes
from . import routes
