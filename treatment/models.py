from dataclasses import dataclass
import datetime
from app import db


@dataclass
class Treatment(db.Model):
    __tablename__ = 'Core_treatment'

    Trt_Id_str: str
    Trt_TrtId_int: int
    Trt_RenderedTrtId_int: int
    Ther_Id_str: str
    TrtStatus_Id_str: str
    Trt_Start_dt: datetime
    Trt_end_dt: datetime
    Trt_CancelationReason_id: int
    Trt_CancelationReason_str: str
    Pat_Id_int: int
    Presc_Id_int: int

    Trt_Id_str = db.Column(db.String())
    Trt_TrtId_int = db.Column(db.Integer(), primary_key=True)
    Trt_RenderedTrtId_int = db.Column(db.Integer(), primary_key=True)
    Ther_Id_str = db.Column(db.String())
    TrtStatus_Id_str = db.Column(db.String())
    Trt_Start_dt = db.Column(db.DateTime())
    Trt_end_dt = db.Column(db.DateTime())
    Trt_CancelationReason_id = db.Column(db.Integer())
    Trt_CancelationReason_str = db.Column(db.String())
    Pat_Id_int = db.Column(db.Integer())
    Presc_Id_int = db.Column(db.Integer())
