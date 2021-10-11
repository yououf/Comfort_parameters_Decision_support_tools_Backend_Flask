from dataclasses import dataclass

from app import db


@dataclass
class SuggestedComfortParams(db.Model):
    __tablename__ = 'DIH_Suggested_Comfort_Param'

    id: int
    patientId: int
    treatmentId: int
    renderedTreatmentId: int
    techId: int
    date: str
    param_ModeAttribute: str
    param_ModeAttributeSetting: int
    param_RampType: str
    param_RampTime: int
    param_RampStartPressure: float
    isAccepted: bool
    
    

    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    patientId = db.Column(db.Integer())
    treatmentId = db.Column(db.Integer())
    renderedTreatmentId = db.Column(db.Integer())
    techId = db.Column(db.Integer())
    date = db.Column(db.DateTime())
    param_ModeAttribute = db.Column(db.String())
    param_ModeAttributeSetting = db.Column(db.Integer())
    param_RampType = db.Column(db.String())
    param_RampTime = db.Column(db.Integer())
    param_RampStartPressure = db.Column(db.Float())
    isAccepted = db.Column(db.Boolean())

    def __init__(self, patient_id, tech_id, date, is_accepted, param_mode_attribute ,param_mode_attribute_setting
    , param_ramp_type, param_ramp_time, param_ramp_start_pressure, treatment_id,rendered_treatment_id):
        self.patientId = patient_id
        self.techId = tech_id
        self.date = date
        self.isAccepted = is_accepted
        self.param_ModeAttribute = param_mode_attribute
        self.param_ModeAttributeSetting =  param_mode_attribute_setting
        self.param_RampType = param_ramp_type
        self.param_RampTime = param_ramp_time
        self.param_RampStartPressure = param_ramp_start_pressure 
        self.treatmentId = treatment_id
        self.renderedTreatmentId = rendered_treatment_id
       
        
