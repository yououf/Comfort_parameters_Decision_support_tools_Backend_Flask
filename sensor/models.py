from dataclasses import dataclass
import datetime
from app import db


@dataclass
class Sensor(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Sensor'

    id_sensor: int
    type: str
    manufacturer_name: str

    id_sensor = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String())
    manufacturer_name = db.Column(db.String())


ExperienceSensor = db.Table('Experience_sensor', db.metadata,
                            db.Column('id_experience', db.Integer, db.ForeignKey('Experience.id_experience')),
                            db.Column('id_sensor_detail', db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
                            )


@dataclass
class SensorDetails(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Sensor_details'

    id_sensor_detail: int
    isActive: bool
    experiences: list

    id_sensor_detail = db.Column(db.Integer(), primary_key=True)
    isActive = db.Column(db.Boolean())
    experiences = db.relationship('Experience', secondary=ExperienceSensor, backref='sensors_detail')


@dataclass
class SensorDetailsNetatmo(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Sensor_details_netatmo'

    id_sensor: int
    id_sensor_detail: int
    id_sensor_netatmo: int
    last_setup: datetime
    type: str
    co2_calibrating: bool
    sensor_name: str
    last_seen: datetime
    last_message: datetime
    wifi_status: int
    firmware: int
    reachable: bool
    date_setup: datetime
    sensor: Sensor
    sensor_detail: SensorDetails

    id_sensor = db.Column(db.Integer(), db.ForeignKey('Sensor.id_sensor'), primary_key=True)
    sensor = db.relationship('Sensor', backref='sensors_detail_netatmo')
    id_sensor_detail = db.Column(db.Integer(), db.ForeignKey('Sensor_details.id_sensor_detail'), primary_key=True)
    sensor_detail = db.relationship('SensorDetails', backref='sensors_detail_netatmo')
    id_sensor_netatmo = db.Column(db.Integer(), primary_key=True)
    last_setup = db.Column(db.DateTime())
    type = db.Column(db.String())
    co2_calibrating = db.Column(db.Boolean())
    sensor_name = db.Column(db.String())
    last_seen = db.Column(db.DateTime())
    last_message = db.Column(db.DateTime())
    wifi_status = db.Column(db.Integer())
    firmware = db.Column(db.Integer())
    reachable = db.Column(db.Boolean())
    date_setup = db.Column(db.DateTime())
