from dataclasses import dataclass

from app import db


@dataclass
class Consumable(db.Model):
    __tablename__ = 'Consumable'

    InterventionId: int
    TreatmentId: int
    RenderedTreatmentId: int
    FamilyId: int
    ModelId: int
    ModelName: str
    Quantity: int

    InterventionId = db.Column(db.Integer(), primary_key=True)
    TreatmentId = db.Column(db.Integer())
    RenderedTreatmentId = db.Column(db.Integer())
    FamilyId = db.Column(db.Integer())
    ModelId = db.Column(db.Integer())
    ModelName = db.Column(db.String())
    Quantity = db.Column(db.Integer())


@dataclass
class Model(db.Model):
    __tablename__ = 'Mat_Model'

    Material_Id_int: int
    Material_Number_str: str
    Material_InTouchId_str: str
    Fam_Id_int: int
    Prov_Id_int: int
    Model_Id_str: str
    Model_Description_str: str
    Model_ProviderRefProduct_str: str
    LPP_Id_str: str
    Model_Therapy_str: str
    Model_TariffType_str: str
    Model_Cost_ft: float
    Material_IsActive_bl: bool

    Material_Id_int = db.Column(db.Integer(), primary_key=True)
    Material_Number_str = db.Column(db.String())
    Material_InTouchId_str = db.Column(db.String())
    Fam_Id_int = db.Column(db.Integer())
    Prov_Id_int = db.Column(db.Integer())
    Model_Id_str = db.Column(db.String())
    Model_Description_str = db.Column(db.String())
    Model_ProviderRefProduct_str = db.Column(db.String())
    LPP_Id_str = db.Column(db.String())
    Model_Therapy_str = db.Column(db.String())
    Model_TariffType_str = db.Column(db.String())
    Model_Cost_ft = db.Column(db.Float())
    Material_IsActive_bl = db.Column(db.Boolean())


@dataclass
class SuggestedMask(db.Model):
    __tablename__ = 'DIH_Suggested_Mask'

    Id: int
    PatientId: int
    TechId: int
    Date: str
    MaskSuggestedId: str
    IsAccepted: bool
    MaskSelectedId: str

    Id = db.Column(db.Integer(), primary_key=True)
    PatientId = db.Column(db.Integer())
    TechId = db.Column(db.Integer())
    Date = db.Column(db.DateTime())
    MaskSuggestedId = db.Column(db.String())
    IsAccepted = db.Column(db.Boolean())
    MaskSelectedId = db.Column(db.String())

    def __init__(self, patient_id, tech_id, date, mask_suggested_id, is_accepted, mask_selected_id):
        self.PatientId = patient_id
        self.TechId = tech_id
        self.Date = date
        self.MaskSuggestedId = mask_suggested_id
        self.IsAccepted = is_accepted
        self.MaskSelectedId = mask_selected_id
