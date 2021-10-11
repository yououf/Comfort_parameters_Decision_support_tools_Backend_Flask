import datetime
from dataclasses import dataclass

from app import db


@dataclass
class Pressure(db.Model):
    __tablename__ = 'pressure'
    __bind_key__ = 'DIH4CPS'

    pressure_id: int
    pressure_lib: str
    value: int
    unity: str
    measure_date: datetime.date
    measure_time: datetime.time
    creation_date: datetime.date
    creation_time: datetime.time

    pressure_id = db.Column(db.Integer, primary_key=True)
    pressure_lib = db.Column(db.String())
    value = db.Column(db.Float)
    unity = db.Column(db.String())
    measure_date = db.Column(db.Date())
    measure_time = db.Column(db.Time())
    creation_date = db.Column(db.Date())
    creation_time = db.Column(db.Time())