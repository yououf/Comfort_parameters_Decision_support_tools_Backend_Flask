from dataclasses import dataclass

from app import db
import datetime


@dataclass
class Address(db.Model):
    __tablename__ = "Core_Address"

    ContactT_Id_int: int
    Ent_Id_int: int
    Add_Index_int: int
    Add_PostalCode_str: str
    City_Name_str: str
    Coun_id_str: str
    Add_IsMain_bl: bool

    ContactT_Id_int = db.Column(db.Integer, primary_key=True)
    Ent_Id_int = db.Column(db.Integer(), db.ForeignKey('Core_Patient.Pat_Id_int'))
    Add_Index_int = db.Column(db.Integer())
    Add_PostalCode_str = db.Column(db.String())
    City_Name_str = db.Column(db.String())
    Coun_id_str = db.Column(db.String())
    Add_IsMain_bl = db.Column(db.Boolean())


@dataclass
class PatientPhilipsScore(db.Model):
    __tablename__ = 'Philips_score'

    Pat_Id_int: int
    Meas_TrtId_int: int
    Meas_Record_dt: int
    Meas_MeasurementAHI_ft: float
    Meas_MeasurementCompliance_ft: float
    Meas_MeasurementLeak_ft: float
    Meas_DeviceTypeId_int: int
    raw_score: float
    score_norm: float
    Meas_MeasurementLeak_score_ft: float
    Meas_MeasurementAHI_score_ft: float
    Meas_MeasurementCompliance_score_ft: float

    Pat_Id_int = db.Column(db.Integer(), db.ForeignKey('Core_Patient.Pat_Id_int'), primary_key=True)
    Meas_TrtId_int = db.Column(db.Integer())
    Meas_Record_dt = db.Column(db.Integer(), primary_key=True)
    Meas_MeasurementAHI_ft = db.Column(db.Float())
    Meas_MeasurementCompliance_ft = db.Column(db.Float())
    Meas_MeasurementLeak_ft = db.Column(db.Float())
    Meas_DeviceTypeId_int = db.Column(db.Integer())
    raw_score = db.Column(db.Float())
    score_norm = db.Column(db.Float())
    Meas_MeasurementLeak_score_ft = db.Column(db.Float())
    Meas_MeasurementAHI_score_ft = db.Column(db.Float())
    Meas_MeasurementCompliance_score_ft = db.Column(db.Float())


@dataclass
class Patient(db.Model):
    __tablename__ = 'Core_Patient'

    Pat_Id_int: int
    Pat_BU_str: str
    Pat_Gender_str: str
    Pat_BirthDate_dt: str
    Pat_IsActive_bl: bool
    Pat_TreatActiveNb_int: int
    address: Address

    Pat_Id_int = db.Column(db.Integer(), primary_key=True)
    Pat_BU_str = db.Column(db.String())
    Pat_Gender_str = db.Column(db.String())
    Pat_BirthDate_dt = db.Column(db.Date())
    Pat_IsActive_bl = db.Column(db.Boolean())
    Pat_TreatActiveNb_int = db.Column(db.Integer())

    address = db.relationship("Address", backref='patient')
    philips_score = db.relationship("PatientPhilipsScore", backref='patient')


@dataclass
class PatientDIH(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Patient_DIH'

    TRC_patient_id: int
    treatment_id: int
    rendered_treatment_id: int

    TRC_patient_id = db.Column(db.Integer(), primary_key=True)
    treatment_id = db.Column(db.Integer())
    rendered_treatment_id = db.Column(db.Integer())


@dataclass
class PatientDetailNetatmo(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Patient_details_netatmo'

    TRC_patient_id: int
    id_patient_netatmo: int
    mail: str
    home_id: str
    home_name: str
    patient_dih: PatientDIH

    TRC_patient_id = db.Column(db.Integer(), db.ForeignKey('Patient_DIH.TRC_patient_id'), primary_key=True)
    patient_dih = db.relationship('PatientDIH', backref='patients_detail_netatmo')
    id_patient_netatmo = db.Column(db.Integer(), primary_key=True)
    mail = db.Column(db.String())
    home_id = db.Column(db.String())
    home_name = db.Column(db.String())


@dataclass
class Experience(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Experience'

    id_experience: int
    TRC_patient_id: int
    start_date: datetime
    end_date: datetime
    patient_dih: PatientDIH

    id_experience = db.Column(db.Integer(), primary_key=True)
    TRC_patient_id = db.Column(db.Integer(), db.ForeignKey('Patient_DIH.TRC_patient_id'))
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    patient_dih = db.relationship('PatientDIH', backref='experiences')


@dataclass
class TokenInformation(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Token_information'

    id: int
    refresh_token: str
    TRC_patient_id: int
    patient_dih: PatientDIH

    id = db.Column(db.Integer(), primary_key=True)
    refresh_token = db.Column(db.String())
    TRC_patient_id = db.Column(db.Integer(), db.ForeignKey('Patient_DIH.TRC_patient_id'))
    patient_dih = db.relationship('PatientDIH', backref='token_information')


@dataclass
class ConnexionInformation(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Connexion_information'

    id: int
    access_date: str
    TRC_patient_id: int
    patient_dih: PatientDIH

    id = db.Column(db.Integer(), primary_key=True)
    access_date = db.Column(db.Integer())
    TRC_patient_id = db.Column(db.Integer(), db.ForeignKey('Patient_DIH.TRC_patient_id'))
    patient_dih = db.relationship('PatientDIH', backref='connexion_information')
