from flask import Blueprint

humidifiers_blueprint = Blueprint('humidifiers', __name__,
                                  url_prefix='/humidifiers/')

# import routes
from . import routes
