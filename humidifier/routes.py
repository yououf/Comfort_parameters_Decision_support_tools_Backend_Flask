# Mask
from flask import jsonify, request
from flask_api import status
import random

from app import db
from humidifier import humidifiers_blueprint
from humidifier.models import SuggestedHumidifier
from patient.routes import patient_is_valid
from equipment.models import Equipment
from treatment.models import Treatment
from treatment import CPAP_TREATMENT_ID, OPEN_TREATMENT
from provider.models import Provider


@humidifiers_blueprint.route('needs_humidifier/<int:patient_id>')
def get_needs_humidifier(patient_id):
    if not patient_is_valid(patient_id):
        return jsonify("Patient introuvable"), status.HTTP_204_NO_CONTENT
    else:
        return jsonify({"needs_humidifier": bool(random.getrandbits(1))})


@humidifiers_blueprint.route('last_CPAP/<int:patient_id>')
def get_last_cpap_id_patient(patient_id):
    if not patient_is_valid(patient_id):
        return jsonify("Patient introuvable"), status.HTTP_204_NO_CONTENT
    else:
        last_rendered_treatment = db.session.query(db.func.max(Treatment.Trt_RenderedTrtId_int),
                                                   Treatment.Trt_TrtId_int).filter(
            Treatment.Pat_Id_int == patient_id, Treatment.TrtStatus_Id_str == OPEN_TREATMENT, Treatment.Ther_Id_str.in_(
                CPAP_TREATMENT_ID)).group_by(Treatment.Trt_TrtId_int).first()
        #list_last_rendered_treatment = list(last_rendered_treatment)
        #list_last_rendered_treatment.sort()
        last_cpap = db.session.query(Equipment).join(Treatment,
                                                     (db.and_(
                                                         Equipment.RenderedTreatmentId == Treatment.Trt_RenderedTrtId_int,
                                                         Equipment.TreatmentId == Treatment.Trt_TrtId_int))).filter(
            Treatment.Pat_Id_int == patient_id, Treatment.TrtStatus_Id_str == OPEN_TREATMENT, Treatment.Ther_Id_str.in_(
                CPAP_TREATMENT_ID), Equipment.RenderedTreatmentId == last_rendered_treatment[0]).first()

        # last_rendered_treatment[0] is the last_rendered_treatment_id of the patient
        # last_rendered_treatment[1] is the last_treatment_id of the patient

        if last_cpap is None:
            return jsonify("Impossible de trouver le dernier traitement"), status.HTTP_204_NO_CONTENT

        provider = db.session.query(Provider).filter(Provider.Prov_Id_int == last_cpap.FabricantId).first()

        if provider is None:
            return jsonify("Impossible de trouver le fabricant"), status.HTTP_204_NO_CONTENT

        json_last_cpap = {
            "Prov_Name_str": provider.Prov_Name_str, "Prov_Id_int": provider.Prov_Id_int,
            "DeliveryDate": last_cpap.DeliveryDate, "ModelName": last_cpap.ModelName, "BarCode": last_cpap.BarCode,
            "NumeroSerie": last_cpap.NumeroSerie, "LastRenderedTreatmentID": last_rendered_treatment[0],
            "TreatmentId": last_rendered_treatment[1]

        }

        return jsonify(json_last_cpap), status.HTTP_200_OK


@humidifiers_blueprint.route('patient/suggested/patient_id/<int:patient_id>', methods=['POST'])
def post_suggested_humidifier(patient_id):
    try:
        json = request.get_json()

        suggested_humidifier = SuggestedHumidifier(patient_id, json["TechId"], json["Date"], json["IsAccepted"],
                                                   json["Param_Humidifier"],
                                                   json["Param_TubeTemperature"],
                                                   json["TreatmentId"], json["LastRenderedTreatmentID"],
                                                   json["IsHumidifierSuggested"])

        db.session.add(suggested_humidifier)
        db.session.commit()

    except AttributeError:
        return jsonify("No json found in the request")

    return jsonify("Successfully created"), status.HTTP_201_CREATED
