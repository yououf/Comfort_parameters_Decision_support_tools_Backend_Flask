# Technicians
from flask import jsonify
from flask_api import status

from technician import technicians_blueprint
from technician.models import Technician, Trip, Intervention


@technicians_blueprint.route('<int:technician_id>')
def get_patient_dih(technician_id):
    technicians = Technician.query.get(technician_id)

    if technicians is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(technicians), status.HTTP_200_OK


@technicians_blueprint.route("/trips/date/<string:date>/technician/<int:technician_id>")
def get_trips_technician(date, technician_id):
    interventions = Intervention.query.join(Trip).join(Technician).filter(Technician.TechId == technician_id,
                                                                          Trip.IsOptimized, Trip.TripDate == date,
                                                                          Intervention.PatientId >= 0).order_by(
        Intervention.ForecastedDate)

    if interventions is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(interventions), status.HTTP_200_OK
