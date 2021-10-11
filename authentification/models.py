from dataclasses import dataclass
import datetime

from app import db

@dataclass
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.user_id'))
    role_id = db.Column('role_id', db.Integer,db.ForeignKey('role.role_id'))


@dataclass
class Role(db.Model):
    __tablename__ = 'role'
    # __bind_key__ = 'DIH4CPS'

    role_id: int
    name: str
    description: str

    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))


@dataclass
class User(db.Model):
    __tablename__ = 'user'

    user_id = int
    email: str
    password: str
    last_login_at: datetime.datetime
    current_login_at: datetime.datetime
    last_login_ip: str
    current_login_ip: str
    login_count: int
    active: int
    roles: int

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.Date())
    current_login_at = db.Column(db.Date())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Integer)
    roles = db.relationship('Role', secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))

    @property
    def serialize(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'roles': [item.name for item in self.roles]
        }
