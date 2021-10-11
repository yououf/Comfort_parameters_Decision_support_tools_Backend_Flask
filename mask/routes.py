# Mask
from flask import jsonify, request
from flask_api import status
import random

from app import db
from mask import masks_blueprint, nasal_pillow_ids, full_face_ids, nasal_ids
from mask.models import Model, Consumable, SuggestedMask
from provider.models import Provider
from technician.models import Intervention


@masks_blueprint.route('face')
def get_full_face_masks():
    return get_masks(full_face_ids)


@masks_blueprint.route('nasal')
def get_nasal_masks():
    return get_masks(nasal_ids)


@masks_blueprint.route('nasal/pillow')
def get_nasal_pillow_mask():
    return get_masks(nasal_pillow_ids)


@masks_blueprint.route('patient/historic/<int:patient_id>')
def get_patient_masks_historic(patient_id):
    masks = db.session.query(Model).join(Consumable, Consumable.ModelId == Model.Model_Id_str).join(Provider,
                                                                                                    Provider.Prov_Id_int == Model.Prov_Id_int).join(
        Intervention,
        Intervention.InterventionId == Consumable.InterventionId).with_entities(
        Model.Material_InTouchId_str, Model.Model_Description_str, Intervention.TRCRealizationDate,
        Intervention.PatientId, Provider.Prov_Name_str).filter(
        Intervention.PatientId == patient_id, Model.Fam_Id_int == 22,
        Intervention.Status == 'E').distinct().order_by(Intervention.TRCRealizationDate.desc()).all()

    if len(masks) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_masks = []

    for mask in masks:
        list_masks.append({
            "id": mask.Material_InTouchId_str, "description": mask.Model_Description_str,
            "date": mask.TRCRealizationDate, "patient_id": mask.PatientId, "provider": mask.Prov_Name_str,
        })

    return jsonify(list_masks), status.HTTP_200_OK


def get_masks(mask_ids):
    masks = db.session.query(Model).join(Provider, Model.Prov_Id_int == Provider.Prov_Id_int).with_entities(
        Provider.Prov_Name_str, Model.Model_Description_str, Model.Material_InTouchId_str, Model.Model_Cost_ft).filter(
        Model.Material_InTouchId_str.in_(
            mask_ids)).distinct().all()

    if len(masks) == 0:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    list_masks = []

    for mask in masks:
        list_masks.append({
            "id": mask.Material_InTouchId_str, "description": mask.Model_Description_str,
            "price": mask.Model_Cost_ft, "provider": mask.Prov_Name_str
        })

    return jsonify(list_masks), status.HTTP_200_OK


@masks_blueprint.route('patient/suggested/<int:patient_id>')
def get_suggested_mask(patient_id):
    list_id_mask = full_face_ids + nasal_ids + nasal_pillow_ids

    rand = random.randint(0, len(list_id_mask) - 1)

    mask = db.session.query(Model).join(Provider, Model.Prov_Id_int == Provider.Prov_Id_int).with_entities(
        Provider.Prov_Name_str, Model.Model_Description_str, Model.Material_InTouchId_str, Model.Model_Cost_ft).filter(
        Model.Material_InTouchId_str ==
        list_id_mask[rand]).first()

    if mask is None:
        return jsonify("Not found"), status.HTTP_204_NO_CONTENT

    mask_json = {
        "id": mask.Material_InTouchId_str, "description": mask.Model_Description_str,
        "price": mask.Model_Cost_ft, "provider": mask.Prov_Name_str
    }

    return jsonify(mask_json), status.HTTP_200_OK


@masks_blueprint.route('patient/suggested/patient_id/<int:patient_id>', methods=['POST'])
def post_suggested_mask(patient_id):
    try:
        json = request.get_json()

        suggested_mask = SuggestedMask(patient_id, json["TechId"], json["Date"], json["MaskSuggestedId"],
                                       json["IsAccepted"], json["MaskSelectedId"])

        db.session.add(suggested_mask)
        db.session.commit()

    except AttributeError:
        return jsonify("No json found in the request")

    return jsonify("Successfully created"), status.HTTP_201_CREATED
