# Patient

from flask import jsonify
from flask_api import status

from app import db

from region import regions_blueprint
from region.models import RegionZipCodes, RegionType, ConfigRegionSecto, ConfigRegion
from patient.models import Patient, PatientPhilipsScore, Address


@regions_blueprint.route('types', methods=['GET'])
def get_type_regions():
    regions_type = RegionType.query.all()

    if regions_type is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(regions_type), status.HTTP_200_OK


@regions_blueprint.route(
    'score/date_debut/<string:date_debut>/date_fin/<string:date_fin>/name/<string:region_name_str>',
    methods=['GET'])
def get_region_score(date_debut, date_fin, region_name_str):
    patient = Patient
    score_patient = PatientPhilipsScore
    address = Address
    config_region = ConfigRegionSecto

    region = ConfigRegion.query.filter(ConfigRegion.Region_Name_str == region_name_str).first()

    region_id_int = region.Region_Id_int

    sub_query = db.session.query(config_region.PostalCodeBegin_str, config_region.PostalCodeEnd_str).filter(
        config_region.Region_Id_int == region_id_int, address.Add_PostalCode_str < config_region.PostalCodeEnd_str,
        address.Add_PostalCode_str > config_region.PostalCodeBegin_str)

    query = db.session.query(db.func.avg(score_patient.raw_score), score_patient.Meas_Record_dt).join(
        patient).join(address).filter(sub_query.exists(), score_patient.Meas_Record_dt > date_debut,
                                      score_patient.Meas_Record_dt < date_fin, ).group_by(
        score_patient.Meas_Record_dt).order_by(score_patient.Meas_Record_dt).all()

    if len(query) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_measures = []

    for measure in query:
        list_measures.append({"raw_score": measure[0],
                              "Meas_Record_dt": measure[1], "region_id_int": region_id_int})

    return jsonify(list_measures), status.HTTP_200_OK


@regions_blueprint.route(
    'leakage/date_debut/<string:date_debut>/date_fin/<string:date_fin>/name/<string:region_name_str>',
    methods=['GET'])
def get_region_mask_leakage(date_debut, date_fin, region_name_str):
    patient = Patient
    score_patient = PatientPhilipsScore
    address = Address
    config_region = ConfigRegionSecto

    region = ConfigRegion.query.filter(ConfigRegion.Region_Name_str == region_name_str).first()

    region_id_int = region.Region_Id_int

    sub_query = db.session.query(config_region.PostalCodeBegin_str, config_region.PostalCodeEnd_str).filter(
        config_region.Region_Id_int == region_id_int, address.Add_PostalCode_str < config_region.PostalCodeEnd_str,
        address.Add_PostalCode_str > config_region.PostalCodeBegin_str)

    query = db.session.query(db.func.avg(score_patient.Meas_MeasurementLeak_ft), score_patient.Meas_Record_dt).join(
        patient).join(address).filter(sub_query.exists(), score_patient.Meas_Record_dt > date_debut,
                                      score_patient.Meas_Record_dt < date_fin, ).group_by(
        score_patient.Meas_Record_dt).order_by(score_patient.Meas_Record_dt).all()

    if len(query) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_measures = []

    for measure in query:
        list_measures.append({"raw_score": measure[0],
                              "Meas_Record_dt": measure[1], "region_id_int": region_id_int})

    return jsonify(list_measures), status.HTTP_200_OK


@regions_blueprint.route(
    'compliance/date_debut/<string:date_debut>/date_fin/<string:date_fin>/name/<string:region_name_str>',
    methods=['GET'])
def get_region_compliance(date_debut, date_fin, region_name_str):
    patient = Patient
    score_patient = PatientPhilipsScore
    address = Address
    config_region = ConfigRegionSecto

    region = ConfigRegion.query.filter(ConfigRegion.Region_Name_str == region_name_str).first()

    region_id_int = region.Region_Id_int

    sub_query = db.session.query(config_region.PostalCodeBegin_str, config_region.PostalCodeEnd_str).filter(
        config_region.Region_Id_int == region_id_int, address.Add_PostalCode_str < config_region.PostalCodeEnd_str,
        address.Add_PostalCode_str > config_region.PostalCodeBegin_str)

    query = db.session.query(db.func.avg(score_patient.Meas_MeasurementCompliance_ft),
                             score_patient.Meas_Record_dt).join(
        patient).join(address).filter(sub_query.exists(), score_patient.Meas_Record_dt > date_debut,
                                      score_patient.Meas_Record_dt < date_fin, ).group_by(
        score_patient.Meas_Record_dt).order_by(score_patient.Meas_Record_dt).all()

    if len(query) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_measures = []

    for measure in query:
        list_measures.append({"raw_score": measure[0],
                              "Meas_Record_dt": measure[1], "region_id_int": region_id_int})

    return jsonify(list_measures), status.HTTP_200_OK


@regions_blueprint.route(
    'ahi/date_debut/<string:date_debut>/date_fin/<string:date_fin>/name/<string:region_name_str>',
    methods=['GET'])
def get_region_ahi(date_debut, date_fin, region_name_str):
    patient = Patient
    score_patient = PatientPhilipsScore
    address = Address
    config_region = ConfigRegionSecto

    region = ConfigRegion.query.filter(ConfigRegion.Region_Name_str == region_name_str).first()

    region_id_int = region.Region_Id_int

    sub_query = db.session.query(config_region.PostalCodeBegin_str, config_region.PostalCodeEnd_str).filter(
        config_region.Region_Id_int == region_id_int, address.Add_PostalCode_str < config_region.PostalCodeEnd_str,
        address.Add_PostalCode_str > config_region.PostalCodeBegin_str)

    query = db.session.query(db.func.avg(score_patient.Meas_MeasurementAHI_ft), score_patient.Meas_Record_dt).join(
        patient).join(address).filter(sub_query.exists(), score_patient.Meas_Record_dt > date_debut,
                                      score_patient.Meas_Record_dt < date_fin, ).group_by(
        score_patient.Meas_Record_dt).order_by(score_patient.Meas_Record_dt).all()

    if len(query) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_measures = []

    for measure in query:
        list_measures.append({"raw_score": measure[0],
                              "Meas_Record_dt": measure[1], "region_id_int": region_id_int})

    return jsonify(list_measures), status.HTTP_200_OK


@regions_blueprint.route('type/name/<string:type_name>', methods=['GET'])
def get_regions_by_type_name(type_name):
    regions = db.session.query(RegionZipCodes.region_name, RegionZipCodes.region_id).filter_by(
        region_type_name=type_name).distinct()

    if regions.count() == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_regions = []

    for region in regions:
        list_regions.append({"region_id": region.region_id,
                             "region_name": region.region_name})

    return jsonify(list_regions), status.HTTP_200_OK


@regions_blueprint.route('type', methods=['GET'])
def get_regions_type_name():
    regions = db.session.query(RegionZipCodes.region_type_name, RegionZipCodes.region_type_id).distinct()

    if regions.count() == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_regions = []

    for region in regions:
        list_regions.append({"region_type_name": region.region_type_name,
                             "region_type_id": region.region_type_id})

    return jsonify(list_regions), status.HTTP_200_OK
