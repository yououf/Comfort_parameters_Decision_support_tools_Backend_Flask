from flask import Blueprint

technicians_blueprint = Blueprint('technicians', __name__,
                                  url_prefix='/technicians/')

# import routes
from . import routes
