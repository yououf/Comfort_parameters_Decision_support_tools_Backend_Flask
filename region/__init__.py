from flask import Blueprint

# import models
from . import models

regions_blueprint = Blueprint('regions', __name__,
                              url_prefix='/regions/')

# import routes
from . import routes
