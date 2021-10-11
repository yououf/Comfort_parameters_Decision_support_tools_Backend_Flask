from flask import jsonify
from flask_api import status

from sensor import sensors_blueprint
from sensor.models import Sensor, ExperienceSensor, SensorDetails
from patient.models import Experience


@sensors_blueprint.route("", methods=['GET'])
def get_sensors():
    sensors = Sensor.query.all()

    return jsonify(sensors), status.HTTP_200_OK


@sensors_blueprint.route("experience/<int:id_experience>", methods=['GET'])
def get_sensors_experience(id_experience):
    experience = Experience.query.get(id_experience)

    return jsonify(experience.SensorDetails), status.HTTP_200_OK
