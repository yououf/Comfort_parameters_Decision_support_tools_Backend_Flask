from flask import Blueprint

comforts_blueprint = Blueprint('comforts', __name__,
                                  url_prefix='/comforts/')

# import routes
from . import routes
