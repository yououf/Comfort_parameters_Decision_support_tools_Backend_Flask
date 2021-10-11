import datetime
from dataclasses import dataclass

from app import db


@dataclass
class Provider(db.Model):
    __tablename__ = 'Mat_Provider'

    Prov_Id_int: int
    Prov_Name_str: str

    Prov_Id_int = db.Column(db.Integer(), primary_key=True)
    Prov_Name_str = db.Column(db.String())
