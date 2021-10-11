from flask import Blueprint

masks_blueprint = Blueprint('masks', __name__,
                            url_prefix='/masks/')

# Initialize mask id
full_face_ids = ["H022151MP0", "H022155NA9", "H022155CN7"]
nasal_ids = ["H022151JG3", "H022119IB3", "H022119MO0", "H022155OI1"]
nasal_pillow_ids = ["H022119OU0"]

# import routes
from . import routes


