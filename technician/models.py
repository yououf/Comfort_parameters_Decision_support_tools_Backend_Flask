from dataclasses import dataclass

from app import db
import datetime

from patient.models import Patient


@dataclass
class Technician(db.Model):
    __tablename__ = "Technician"

    TechId: int
    ProfileId: int
    VehiculeTypeId: int
    DefaultRegionId: int
    LastName: str
    FirstName: str
    Initials: str
    StartDate: datetime
    EndDate: datetime
    StartHourMail: datetime
    FinishHourMail: datetime
    StartingPointId: int
    EndingPointId: int
    IsLoxTechnician: bool
    IsPdaHS: bool
    StartHourJ1: datetime
    FinishHourJ1: datetime
    SpeedFactor: float
    JobPerDayTarget: int
    OtherParticularities: str
    LongTermTripId: int
    ExportTechId: int
    HasMaps: str
    MealDuration: int
    HasStats: str
    WorkDuration: int
    WorkDurationFriday: int
    WorkDurationSaturday: int
    PreferedBranchAgency: int
    Email: str
    EmailCopy: str
    Phone: str
    PackageType: str

    AgencyMonday: int
    AgencyMondayDuration: int
    StartHourMonday: datetime
    CommentMonday: str

    AgencyTuesday: int
    AgencyTuesdayDuration: int
    StartHourTuesday: datetime
    CommentTuesday: str

    AgencyWednesday: int
    AgencyWednesdayDuration: int
    StartHourWednesday: datetime
    CommentWednesday: str

    AgencyThursday: int
    AgencyThursdayDuration: int
    StartHourThursday: datetime
    CommentThursday: str

    AgencyFriday: int
    AgencyFridayDuration: int
    StartHourFriday: datetime
    CommentFriday: str

    AgencySatursday: int
    AgencySatursdayDuration: int
    StartHourSatursday: datetime
    CommentSatursday: str

    RegionMonday: int
    Regiontuesday: int
    RegionWednesday: int
    Regionthursday: int
    RegionFriday: int
    Regionsaturday: int

    TechId = db.Column(db.Integer(), primary_key=True)
    ProfileId = db.Column(db.Integer())
    VehiculeTypeId = db.Column(db.Integer())
    DefaultRegionId = db.Column(db.Integer())
    LastName = db.Column(db.String())
    FirstName = db.Column(db.String())
    Initials = db.Column(db.String())
    StartDate = db.Column(db.DateTime())
    EndDate = db.Column(db.DateTime())
    StartHourMail = db.Column(db.DateTime())
    FinishHourMail = db.Column(db.DateTime())
    StartingPointId = db.Column(db.Integer())
    EndingPointId = db.Column(db.Integer())
    IsLoxTechnician = db.Column(db.Boolean())
    IsPdaHS = db.Column(db.Boolean())
    StartHourJ1 = db.Column(db.DateTime())
    FinishHourJ1 = db.Column(db.DateTime())
    SpeedFactor = db.Column(db.Float())
    JobPerDayTarget = db.Column(db.Integer())
    OtherParticularities = db.Column(db.String())
    LongTermTripId = db.Column(db.Integer())
    ExportTechId = db.Column(db.Integer())
    HasMaps = db.Column(db.String())
    MealDuration = db.Column(db.Integer())
    HasStats = db.Column(db.String())
    WorkDuration = db.Column(db.Integer())
    WorkDurationFriday = db.Column(db.Integer())
    WorkDurationSaturday = db.Column(db.Integer())
    PreferedBranchAgency = db.Column(db.Integer())
    Email = db.Column(db.String())
    EmailCopy = db.Column(db.String())
    Phone = db.Column(db.String())
    PackageType = db.Column(db.String())

    AgencyMonday = db.Column(db.Integer())
    AgencyMondayDuration = db.Column(db.Integer())
    StartHourMonday = db.Column(db.DateTime())
    CommentMonday = db.Column(db.String())

    AgencyTuesday = db.Column(db.Integer())
    AgencyTuesdayDuration = db.Column(db.Integer())
    StartHourTuesday = db.Column(db.DateTime())
    CommentTuesday = db.Column(db.String())

    AgencyWednesday = db.Column(db.Integer())
    AgencyWednesdayDuration = db.Column(db.Integer())
    StartHourWednesday = db.Column(db.DateTime())
    CommentWednesday = db.Column(db.String())

    AgencyThursday = db.Column(db.Integer())
    AgencyThursdayDuration = db.Column(db.Integer())
    StartHourThursday = db.Column(db.DateTime())
    CommentThursday = db.Column(db.String())

    AgencyFriday = db.Column(db.Integer())
    AgencyFridayDuration = db.Column(db.Integer())
    StartHourFriday = db.Column(db.DateTime())
    CommentFriday = db.Column(db.String())

    AgencySatursday = db.Column(db.Integer())
    AgencySatursdayDuration = db.Column(db.Integer())
    StartHourSatursday = db.Column(db.DateTime())
    CommentSatursday = db.Column(db.String())

    RegionMonday = db.Column(db.Integer())
    Regiontuesday = db.Column(db.Integer())
    RegionWednesday = db.Column(db.Integer())
    Regionthursday = db.Column(db.Integer())
    RegionFriday = db.Column(db.Integer())
    Regionsaturday = db.Column(db.Integer())


@dataclass
class Trip(db.Model):
    __tablename__ = "Trip"

    TripId: int
    TechId: int
    TripDate: datetime
    IsOptimized: bool
    StartHour: datetime
    FinishHour: datetime
    LunchTime: datetime
    TripType: str
    TripComment: str
    Kms: float
    TrcExpedId: int
    Done: bool
    technician: Technician

    TripId = db.Column(db.Integer(), primary_key=True)
    TechId = db.Column(db.Integer(), db.ForeignKey('Technician.TechId'))
    technician = db.relationship("Technician", backref="trips")
    TripDate = db.Column(db.DateTime())
    IsOptimized = db.Column(db.Boolean())
    StartHour = db.Column(db.DateTime())
    FinishHour = db.Column(db.DateTime())
    LunchTime = db.Column(db.DateTime())
    TripType = db.Column(db.String())
    TripComment = db.Column(db.String())
    Kms = db.Column(db.Float())
    TrcExpedId = db.Column(db.Integer())
    Done = db.Column(db.Boolean())


@dataclass
class Intervention(db.Model):
    __tablename__ = 'Intervention'

    InterventionId: int
    PatientId: int
    RegionId: int
    AddressId: int
    TripId: int
    TreatmentId: int
    RenderedTreatmentId: int
    Site: str
    ForecastedDate: datetime
    Agreed: str
    Letter: str
    DeliveryWindStart: str
    DeliveryWindEnd: str
    Therapy: str
    ServiceType: str
    Duration: int
    OrderInTrip: int
    LetterSent: str
    Status: str
    LastOptimizationDate: str
    OptimizationCount: int
    Comment: str
    MandatoryTechId: str
    PrescId: str
    TrcForecastedDate: datetime
    PdaStatus: str
    RequestId: int
    Pathology: str
    TrcComment: str
    TrcAgreed: str
    TreatmentStatus: str
    OnHold: bool
    OnHoldUntil: str
    NewTttReason: int
    SmsStatus: int
    TRCRealizationDate: str
    ModemIssue: str
    NoModem: str
    trip: Trip
    patient: Patient

    InterventionId = db.Column(db.Integer(), primary_key=True)
    PatientId = db.Column(db.Integer(), db.ForeignKey("Core_Patient.Pat_Id_int"))
    patient = db.relationship("Patient", backref="patient")
    RegionId = db.Column(db.Integer())
    AddressId = db.Column(db.Integer())
    TripId = db.Column(db.Integer(), db.ForeignKey("Trip.TripId"))
    trip = db.relationship("Trip", backref="interventions")
    TreatmentId = db.Column(db.Integer())
    RenderedTreatmentId = db.Column(db.Integer())
    Site = db.Column(db.String())
    ForecastedDate = db.Column(db.DateTime())
    Agreed = db.Column(db.String())
    Letter = db.Column(db.String())
    DeliveryWindStart = db.Column(db.DateTime())
    DeliveryWindEnd = db.Column(db.DateTime())
    Therapy = db.Column(db.String())
    ServiceType = db.Column(db.String())
    Duration = db.Column(db.Integer())
    OrderInTrip = db.Column(db.Integer())
    LetterSent = db.Column(db.DateTime())
    Status = db.Column(db.String())
    LastOptimizationDate = db.Column(db.DateTime())
    OptimizationCount = db.Column(db.Integer())
    Comment = db.Column(db.String())
    MandatoryTechId = db.Column(db.String())
    PrescId = db.Column(db.String())
    TrcForecastedDate = db.Column(db.DateTime())
    PdaStatus = db.Column(db.String())
    RequestId = db.Column(db.Integer())
    Pathology = db.Column(db.String())
    TrcComment = db.Column(db.String())
    TrcAgreed = db.Column(db.String())
    TreatmentStatus = db.Column(db.String())
    OnHold = db.Column(db.Boolean())
    OnHoldUntil = db.Column(db.DateTime())
    NewTttReason = db.Column(db.Integer())
    SmsStatus = db.Column(db.Integer())
    TRCRealizationDate = db.Column(db.DateTime())
    ModemIssue = db.Column(db.String())
    NoModem = db.Column(db.String())
