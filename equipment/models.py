import datetime
from dataclasses import dataclass

from app import db


@dataclass
class Equipment(db.Model):
    __tablename__ = 'Equipment'

    TreatmentId: int
    RenderedTreatmentId: int
    FamilyId: int
    FabricantId: int
    EquipmentId: int
    NumeroSerie: int
    BarCode: str
    DeliveryDate: datetime
    ModelName: str

    TreatmentId = db.Column(db.Integer())
    RenderedTreatmentId = db.Column(db.Integer())
    FamilyId = db.Column(db.Integer())
    FabricantId = db.Column(db.Integer())
    EquipmentId = db.Column(db.Integer(), primary_key=True)
    NumeroSerie = db.Column(db.Integer())
    BarCode = db.Column(db.String())
    DeliveryDate = db.Column(db.DateTime())
    ModelName = db.Column(db.String())
