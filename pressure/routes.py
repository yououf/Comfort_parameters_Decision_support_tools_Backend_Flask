# Pressure
from flask import jsonify
from flask_api import status

from pressure import pressure_blueprint
from pressure.models import Pressure


@pressure_blueprint.route('')
def get_pressures():
    pressures = Pressure.query.all()
    return jsonify(pressures), status.HTTP_200_OK