from dataclasses import dataclass

from app import db


@dataclass
class RegionZipCodes(db.Model):
    __tablename__ = 'region_zip_codes'

    id: int
    region_id: int
    region_name: str
    region_type_id: int
    region_type_name: str
    zip_code_start: str
    zip_code_end: str

    id = db.Column(db.Integer(), primary_key=True)
    region_id = db.Column(db.Integer())
    region_name = db.Column(db.String())
    region_type_id = db.Column(db.Integer())
    region_type_name = db.Column(db.String())
    zip_code_start = db.Column(db.String())
    zip_code_end = db.Column(db.String())


@dataclass
class RegionType(db.Model):
    __tablename__ = 'Config_RegionType'

    RegType_Id_int: int
    RegType_Name_str: str

    RegType_Id_int = db.Column(db.Integer(), primary_key=True)
    RegType_Name_str = db.Column(db.String())


@dataclass
class ConfigRegionSecto(db.Model):
    __tablename__ = 'Config_RegionSecto'

    Region_Id_int: int
    RegType_Id_int: int
    PostalCodeBegin_str: str
    PostalCodeEnd_str: str
    RegSecto_Comment_str: str

    Region_Id_int = db.Column(db.Integer(), primary_key=True)
    RegType_Id_int = db.Column(db.Integer())
    PostalCodeBegin_str = db.Column(db.Integer(), primary_key=True)
    PostalCodeEnd_str = db.Column(db.Integer(), primary_key=True)
    RegSecto_Comment_str = db.Column(db.String())


@dataclass
class ConfigRegion(db.Model):
    __tablename__ = 'Config_Region'

    Region_Id_int: int
    Region_Name_str: str
    Region_IsDisplayed_bl: bool
    RegType_Id_int: int

    Region_Id_int = db.Column(db.Integer(), primary_key=True)
    Region_Name_str = db.Column(db.String())
    Region_IsDisplayed_bl = db.Column(db.Boolean())
    RegType_Id_int = db.Column(db.Integer())
