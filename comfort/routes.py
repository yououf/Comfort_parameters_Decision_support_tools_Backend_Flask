# Mask
from flask import jsonify, request
from flask_api import status
import random

from app import db
from comfort import comforts_blueprint
from comfort.models import SuggestedComfortParams
from patient.routes import patient_is_valid
from equipment.models import Equipment
from treatment.models import Treatment
from treatment import CPAP_TREATMENT_ID, OPEN_TREATMENT
from provider.models import Provider


# route which is used to mocquer the suggestion of the comfort parameters in the event that the parameters will be collected from the source (Suggestion model)
@comforts_blueprint.route('suggested/param/<int:patient_id>', methods=['GET'])
def get_suggested_param_comfort_by_pat_id_(patient_id):
    suggested_param_comfort = SuggestedComfortParams(1,1,"2021-06-03 22:21:44.000",True,"C-Flex",2,"Linear",5,20.0,2,1)
    if suggested_param_comfort is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    return jsonify(suggested_param_comfort), status.HTTP_200_OK

@comforts_blueprint.route('last_CPAP/<int:patient_id>')
def get_last_cpap_id_patient(patient_id):
    if not patient_is_valid(patient_id):
        return jsonify("Patient not exist"), status.HTTP_204_NO_CONTENT
    last_rendered_treatment = db.session.query(db.func.max(Treatment.Trt_RenderedTrtId_int),
                                               Treatment.Trt_TrtId_int).filter(
        Treatment.Pat_Id_int == patient_id, Treatment.TrtStatus_Id_str == OPEN_TREATMENT, Treatment.Ther_Id_str.in_(
            CPAP_TREATMENT_ID)).group_by(Treatment.Trt_TrtId_int).first()

    last_cpap = db.session.query(Equipment).join(Treatment,
                                                 (db.and_(
                                                     Equipment.RenderedTreatmentId == Treatment.Trt_RenderedTrtId_int,
                                                     Equipment.TreatmentId == Treatment.Trt_TrtId_int))).filter(
        Treatment.Pat_Id_int == patient_id, Treatment.TrtStatus_Id_str == OPEN_TREATMENT, Treatment.Ther_Id_str.in_(
            CPAP_TREATMENT_ID), Equipment.RenderedTreatmentId == last_rendered_treatment[0]).first()

    # last_rendered_treatment[0] is the last_rendered_treatment_id of the patient
    # last_rendered_treatment[1] is the last_treatment_id of the patient

    if last_cpap is None:
        return jsonify("Impossible to find the last treatment"), status.HTTP_204_NO_CONTENT

    provider = db.session.query(Provider).filter(Provider.Prov_Id_int == last_cpap.FabricantId).first()

    if provider is None:
        return jsonify("Impossible to find the provider"), status.HTTP_204_NO_CONTENT

    json_last_cpap = {
        "Prov_Name_str": provider.Prov_Name_str, "Prov_Id_int": provider.Prov_Id_int,
        "DeliveryDate": last_cpap.DeliveryDate, "ModelName": last_cpap.ModelName, "BarCode": last_cpap.BarCode,
        "NumeroSerie": last_cpap.NumeroSerie, "LastRenderedTreatmentID": last_rendered_treatment[0],
        "TreatmentId": last_rendered_treatment[1]

    }

    return jsonify(json_last_cpap), status.HTTP_200_OK


@comforts_blueprint.route('patient/suggested_param/patient_id/<int:patient_id>', methods=['POST'])
def post_suggested_comfort_params(patient_id):
    try:
        json = request.get_json()
        suggested_comfort_params = SuggestedComfortParams(patient_id, json["TechId"], json["Date"], json["IsAccepted"],
                                                   json["Param_Mode_Attribute"],
                                                   json["Param_Mode_Attribute_Setting"],
                                                   json["Param_Ramp_Type"],
                                                   json["Param_Ramp_Time"],
                                                   json["Param_Ramp_Start_Pressure"],
                                                   json["TreatmentId"], json["LastRenderedTreatmentID"])

        db.session.add(suggested_comfort_params)
        db.session.commit()

    except AttributeError:
        return jsonify("No json found in the request"), status.HTTP_204_NO_CONTENT

    return jsonify("Successfully created"), status.HTTP_201_CREATED
