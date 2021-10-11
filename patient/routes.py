# Patient
from flask import jsonify
from flask_api import status

from app import db
from patient import patients_blueprint
from patient.models import Patient, PatientPhilipsScore, PatientDIH, Address
from region.models import ConfigRegion, ConfigRegionSecto


def patient_is_valid(id_patient):
    patient = Patient.query.filter(Patient.Pat_Id_int == id_patient).first()

    if patient is None:
        return False
    else:
        return True


@patients_blueprint.route('test')
def test():
    patients = Patient.query.filter(Patient.Pat_Id_int == 72425).first()

    if patients is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(patients), status.HTTP_200_OK


@patients_blueprint.route('')
def get_patients():
    patients = Patient.query.all()

    if patients is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(patients), status.HTTP_200_OK


@patients_blueprint.route('score/date_debut/<string:date_debut>/date_fin/<string:date_fin>/id/<int:pat_id_int>',
                          methods=['GET'])
def get_patient_score(date_debut, date_fin, pat_id_int):
    patient = db.session.query(PatientPhilipsScore).filter(
        PatientPhilipsScore.Pat_Id_int == pat_id_int, PatientPhilipsScore.Meas_Record_dt > date_debut,
        PatientPhilipsScore.Meas_Record_dt < date_fin)
    return jsonify(patient), status.HTTP_200_OK

    list_measures = []

    for measure in patient:
        list_measures.append({"Pat_Id_int": measure.Pat_Id_int, "raw_score": measure.raw_score,
                              "Meas_Record_dt": measure.Meas_Record_dt})

    if len(list_measures) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(list_measures), status.HTTP_200_OK


@patients_blueprint.route('compliance/date_debut/<string:date_debut>/date_fin/<string:date_fin>/id/<int:pat_id_int>',
                          methods=['GET'])
def get_patient_compliance(date_debut, date_fin, pat_id_int):
    patient = db.session.query(PatientPhilipsScore).filter(
        PatientPhilipsScore.Pat_Id_int == pat_id_int, PatientPhilipsScore.Meas_Record_dt > date_debut,
        PatientPhilipsScore.Meas_Record_dt < date_fin)

    list_measures = []

    for measure in patient:
        list_measures.append({"Pat_Id_int": measure.Pat_Id_int, "value": measure.Meas_MeasurementCompliance_ft,
                              "Meas_Record_dt": measure.Meas_Record_dt})

    if len(list_measures) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(list_measures), status.HTTP_200_OK


@patients_blueprint.route('leakage/date_debut/<string:date_debut>/date_fin/<string:date_fin>/id/<int:pat_id_int>',
                          methods=['GET'])
def get_patient_leakage(date_debut, date_fin, pat_id_int):
    patient = db.session.query(PatientPhilipsScore).filter(
        PatientPhilipsScore.Pat_Id_int == pat_id_int, PatientPhilipsScore.Meas_Record_dt > date_debut,
        PatientPhilipsScore.Meas_Record_dt < date_fin)

    list_measures = []

    for measure in patient:
        list_measures.append({"Pat_Id_int": measure.Pat_Id_int, "value": measure.Meas_MeasurementLeak_ft,
                              "Meas_Record_dt": measure.Meas_Record_dt})

    if len(list_measures) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(list_measures), status.HTTP_200_OK


@patients_blueprint.route('ahi/date_debut/<string:date_debut>/date_fin/<string:date_fin>/id/<int:pat_id_int>',
                          methods=['GET'])
def get_patient_ahi(date_debut, date_fin, pat_id_int):
    patient = db.session.query(PatientPhilipsScore).filter(
        PatientPhilipsScore.Pat_Id_int == pat_id_int, PatientPhilipsScore.Meas_Record_dt > date_debut,
        PatientPhilipsScore.Meas_Record_dt < date_fin)

    list_measures = []

    for measure in patient:
        list_measures.append({"Pat_Id_int": measure.Pat_Id_int, "value": measure.Meas_MeasurementAHI_ft,
                              "Meas_Record_dt": measure.Meas_Record_dt})

    if len(list_measures) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(list_measures), status.HTTP_200_OK


@patients_blueprint.route('<int:pat_id_int>', methods=['GET'])
def get_patient_by_pat_id_int(pat_id_int):
    patient = Patient.query.filter_by(Pat_Id_int=pat_id_int)

    if patient.count() == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    if patient.count() > 1:
        return jsonify("Conflict"), status.HTTP_409_CONFLICT

    return jsonify(patient[0]), status.HTTP_200_OK


@patients_blueprint.route('<int:pat_id_int>/region/name', methods=['GET'])
def get_patient_first_region_by_pat_id_int(pat_id_int):
    config_region = db.session.query(ConfigRegion.Region_Name_str, ConfigRegionSecto.Region_Id_int,
                                     Address.Ent_Id_int).filter(
        ConfigRegion.Region_Id_int == ConfigRegionSecto.Region_Id_int, Address.Ent_Id_int == pat_id_int,
        Address.Add_PostalCode_str > ConfigRegionSecto.PostalCodeBegin_str,
        Address.Add_PostalCode_str < ConfigRegionSecto.PostalCodeEnd_str).first()

    if config_region is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    config_region = {'region_name': config_region[0], }

    return jsonify(config_region), status.HTTP_200_OK


@patients_blueprint.route('dih/<int:patient_id>')
def get_patient_dih(patient_id):
    patients = PatientDIH.query.get(patient_id)

    if patients is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(patients), status.HTTP_200_OK
