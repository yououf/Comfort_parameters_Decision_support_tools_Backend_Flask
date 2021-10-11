from flask import jsonify
from flask_api import status
from app import db

from environmental_data import environmental_data_blueprint
from environmental_data.models import Humidity, AbsolutePressure, Co2Level, Noise, Temperature
from sensor.models import SensorDetails, ExperienceSensor
from patient.models import PatientDIH, Experience


@environmental_data_blueprint.route("indoor_temperature/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
                                    methods=['GET'])
def get_indoor_temperature_by_patient_id(begin_date, end_date, id_patient):
    temperatures = Temperature.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Temperature.measure_date <= end_date,
        Temperature.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(temperatures), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "outdoor_temperature/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
    methods=['GET'])
def get_outdoor_temperature_by_patient_id(begin_date, end_date, id_patient):
    temperatures = Temperature.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Temperature.measure_date <= end_date,
        Temperature.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(temperatures), status.HTTP_200_OK


@environmental_data_blueprint.route("indoor_co2_level/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
                                    methods=['GET'])
def get_indoor_co2_level_by_patient_id(begin_date, end_date, id_patient):
    co2_level = Co2Level.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Co2Level.measure_date <= end_date,
        Co2Level.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(co2_level), status.HTTP_200_OK


@environmental_data_blueprint.route("indoor_noise/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
                                    methods=['GET'])
def get_indoor_noise_by_patient_id(begin_date, end_date, id_patient):
    noise = Noise.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Noise.measure_date <= end_date,
        Noise.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(noise), status.HTTP_200_OK


@environmental_data_blueprint.route("indoor_pressure/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
                                    methods=['GET'])
def get_indoor_pressure_by_patient_id(begin_date, end_date, id_patient):
    pressure = AbsolutePressure.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, AbsolutePressure.measure_date <= end_date,
        AbsolutePressure.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(pressure), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_outdoor_temperature/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_outdoor_temperature(id_patient):
    last_temperature = db.session.query(db.func.max(Temperature.id)).join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, SensorDetails.id_sensor_detail == 1).first()

    temperatures = Temperature.query.get(last_temperature)

    return jsonify(temperatures), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_indoor_temperature/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_indoor_temperature(id_patient):
    last_temperature = db.session.query(db.func.max(Temperature.id)).join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, SensorDetails.id_sensor_detail == 1).first()

    temperature = Temperature.query.get(last_temperature)

    return jsonify(temperature), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_indoor_humidity/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_indoor_humidity(id_patient):
    last_humidity = db.session.query(db.func.max(Humidity.id)).join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, SensorDetails.id_sensor_detail == 1).first()

    humidity = Humidity.query.get(last_humidity)

    return jsonify(humidity), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_outdoor_humidity/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_outdoor_humidity(id_patient):
    last_humidity = db.session.query(db.func.max(Humidity.id)).join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, SensorDetails.id_sensor_detail == 1).first()

    humidity = Humidity.query.get(last_humidity)

    return jsonify(humidity), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_noise/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_noise(id_patient):
    last_noise = db.session.query(db.func.max(Noise.id)).join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient).first()

    noise = Noise.query.get(last_noise)

    return jsonify(noise), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_absolute_pressure/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_absolute_pressure(id_patient):
    last_absolute_pressure = db.session.query(db.func.max(AbsolutePressure.id)).join(SensorDetails).join(
        ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient).first()

    absolute_pressure = AbsolutePressure.query.get(last_absolute_pressure)

    return jsonify(absolute_pressure), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "last_co2_level/patient/<int:id_patient>",
    methods=['GET'])
def get_patient_last_co2_level(id_patient):
    last_co2_level = db.session.query(db.func.max(Co2Level.id)).join(SensorDetails).join(
        ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient).first()

    co2_level = Co2Level.query.get(last_co2_level)

    return jsonify(co2_level), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "outdoor_humidity/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
    methods=['GET'])
def get_outdoor_humidity_by_patient_id(begin_date, end_date, id_patient):
    humidity = Humidity.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Humidity.measure_date <= end_date,
        Humidity.measure_date >= begin_date, SensorDetails.id_sensor_detail == 2)

    return jsonify(humidity), status.HTTP_200_OK


@environmental_data_blueprint.route(
    "indoor_humidity/<string:begin_date>/<string:end_date>/patient/<int:id_patient>",
    methods=['GET'])
def get_indoor_humidity_by_patient_id(begin_date, end_date, id_patient):
    humidity = Humidity.query.join(SensorDetails).join(ExperienceSensor).join(
        Experience).join(
        PatientDIH).filter(
        PatientDIH.TRC_patient_id == id_patient, Humidity.measure_date <= end_date,
        Humidity.measure_date >= begin_date, SensorDetails.id_sensor_detail == 1)

    return jsonify(humidity), status.HTTP_200_OK


@environmental_data_blueprint.route("sensor_details/humidities/<int:sensor_detail_id>", methods=['GET'])
def get_humidity_from_sensor_detail(sensor_detail_id):
    # sensor_detail = SensorDetails.query.get(sensor_detail_id)

    patient = PatientDIH.query.get(1)

    return jsonify(patient.experiences[0].sensors_detail[0].humidities), status.HTTP_200_OK
