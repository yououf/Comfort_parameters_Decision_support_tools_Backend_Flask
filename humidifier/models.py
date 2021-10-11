from dataclasses import dataclass

from app import db


@dataclass
class SuggestedHumidifier(db.Model):
    __tablename__ = 'DIH_Suggested_Humidifier'

    Id: int
    PatientId: int
    TechId: int
    Date: str
    Param_TubeTemperature: int
    Param_Humidifier: int
    IsAccepted: bool
    IsHumidifierSuggested: bool
    TreatmentId: int
    RenderedTreatmentId: int

    Id = db.Column(db.Integer(), primary_key=True)
    PatientId = db.Column(db.Integer())
    TreatmentId = db.Column(db.Integer())
    RenderedTreatmentId = db.Column(db.Integer())
    TechId = db.Column(db.Integer())
    Date = db.Column(db.DateTime())
    Param_TubeTemperature = db.Column(db.Integer())
    IsAccepted = db.Column(db.Boolean())
    IsHumidifierSuggested = db.Column(db.Boolean())
    Param_Humidifier = db.Column(db.Integer())

    def __init__(self, patient_id, tech_id, date, is_accepted, param_humidifier, param_tube_temperature, treatment_id,
                 rendered_treatment_id, is_humidifier_suggested):
        self.PatientId = patient_id
        self.TechId = tech_id
        self.RenderedTreatmentId = rendered_treatment_id
        self.TreatmentId = treatment_id
        self.Date = date
        self.Param_TubeTemperature = param_tube_temperature
        self.IsAccepted = is_accepted
        self.IsHumidifierSuggested = is_humidifier_suggested
        self.Param_Humidifier = param_humidifier
