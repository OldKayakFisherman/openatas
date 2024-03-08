from flask_sqlalchemy import SQLAlchemy

from . import db

class Role(db.Model):

    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self) -> str:
        return f'<Role {self.name}>'
    

class User(db.Model):

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))

    def __repr__(self) -> str:
        return f'<User {self.username}>'
    

class OperatingDivision(db.Model):

    __tablename__ = "operating_divisions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    acronym = db.Column(db.String(10))
    

class CFDAMappings(db.Model):

    __tablename__ = "cfda_mappings"

    id = db.Column(db.Integer, primary_key=True)
    cfda_prefix = db.Column(db.String(10))
    cfda_ext = db.Column(db.String(20))
    division_id = db.Column(db.Integer, db.ForeignKey("operating_divisions.id"))
    division = db.relationship("OperatingDivision", backref="cfda_mappings")
