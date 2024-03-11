from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db

class Role(db.Model):

    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


    def __repr__(self) -> str:
        return f'<Role {self.name}>'
    

class User(UserMixin, db.Model):

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, index=True)
    username = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(256))
    approved = db.Column(db.Boolean)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    role = db.relationship("Role", backref="users")

    @property
    def password(self):
        raise AttributeError('password is not a readable property')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

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


class NotificationQueue(db.Model):

    __tablename__ = "notification_queue"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40))
    date_sent = db.Column(db.DateTime)
    date_queued = db.Column(db.DateTime)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)

class NotificationQueueAttachment(db.Model):

    __tablename__ = "notification_queue_attachments"

    id = db.Column(db.Integer, primary_key=True)
    mime_type = db.Column(db.String(40))
    extension = db.Column(db.String(10))
    filename = db.Column(db.String(255))
    filecontents = db.Column(db.LargeBinary)
    notification_id = db.Column(db.Integer, db.ForeignKey("notification_queue.id"))
    notification = db.relationship("NotificationQueue", backref="notification_queue_attachments")

class StoredDocuments(db.Model):

    __tablename__ = "stored_documents"

    id = db.Column(db.Integer, primary_key=True)
    mime_type = db.Column(db.String(40))
    extension = db.Column(db.String(10))
    filename = db.Column(db.String(255))
    filecontents = db.Column(db.LargeBinary)

class AuditLog(db.Model):
    
    __tablename__ = "event_logs"
 

    id = db.Column(db.Integer, primary_key=True, index=True)
    host = db.Column(db.String, nullable=False)
    message = db.Column(db.String)
    severity = db.Column(db.String)
    type = db.Column(db.String)
    whencreated = db.Column(db.DateTime)
    whocreated = db.Column(db.String)
    success = db.Column(db.Boolean)
    source= db.Column(db.String)
    request_headers= db.Column(db.String)
    clientversion= db.Column(db.String)
    backendversion= db.Column(db.String) 



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
