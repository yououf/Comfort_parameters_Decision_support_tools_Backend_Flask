import datetime
from dataclasses import dataclass
from app import db
from sensor.models import SensorDetails


@dataclass
class Temperature(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Temperature'
    id: int
    min_temp: float
    max_temp: float
    date_max_temp: datetime
    date_min_temp: datetime
    unity: str
    measure_date: datetime
    database_date: datetime
    value_data: float
    id_sensor_detail: int
    sensor_details: SensorDetails

    id = db.Column(db.Integer(), primary_key=True)
    min_temp = db.Column(db.Float())
    max_temp = db.Column(db.Float())
    date_min_temp = db.Column(db.DateTime())
    date_max_temp = db.Column(db.DateTime())
    unity = db.Column(db.String())
    measure_date = db.Column(db.DateTime())
    database_date = db.Column(db.DateTime())
    value_data = db.Column(db.Float())
    id_sensor_detail = db.Column(db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
    sensor_details = db.relationship('SensorDetails', backref='temperatures')


@dataclass
class Noise(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Noise'

    id: int
    unity: str
    measure_date: datetime
    database_date: datetime
    value_data: float
    id_sensor_detail: int
    sensor_details: SensorDetails

    id = db.Column(db.Integer(), primary_key=True)
    unity = db.Column(db.String())
    measure_date = db.Column(db.DateTime())
    database_date = db.Column(db.DateTime())
    value_data = db.Column(db.Float())
    id_sensor_detail = db.Column(db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
    sensor_details = db.relationship('SensorDetails', backref='noises')


@dataclass
class Co2Level(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Co2_level'

    id: int
    unity: str
    measure_date: datetime
    database_date: datetime
    value_data: float
    id_sensor_detail: int
    sensor_details: SensorDetails

    id = db.Column(db.Integer(), primary_key=True)
    unity = db.Column(db.String())
    measure_date = db.Column(db.DateTime())
    database_date = db.Column(db.DateTime())
    value_data = db.Column(db.Float())
    id_sensor_detail = db.Column(db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
    sensor_details = db.relationship('SensorDetails', backref='co2_levels')


@dataclass
class Humidity(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'Humidity'

    id: int
    unity: str
    measure_date: datetime
    database_date: datetime
    value_data: float
    id_sensor_detail: int
    sensor_details: SensorDetails

    id = db.Column(db.Integer(), primary_key=True)
    unity = db.Column(db.String())
    measure_date = db.Column(db.DateTime())
    database_date = db.Column(db.DateTime())
    value_data = db.Column(db.Float())
    id_sensor_detail = db.Column(db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
    sensor_details = db.relationship('SensorDetails', backref='humidities')


@dataclass
class AbsolutePressure(db.Model):
    __bind_key__ = 'DIH4CPS'
    __tablename__ = 'AbsolutePressure'

    id: int
    unity: str
    measure_date: datetime
    database_date: datetime
    value_data: float
    id_sensor_detail: int
    sensor_details: SensorDetails

    id = db.Column(db.Integer(), primary_key=True)
    unity = db.Column(db.String())
    measure_date = db.Column(db.DateTime())
    database_date = db.Column(db.DateTime())
    value_data = db.Column(db.Float())
    id_sensor_detail = db.Column(db.Integer, db.ForeignKey('Sensor_details.id_sensor_detail'))
    sensor_details = db.relationship('SensorDetails', backref='absolute_pressure')
