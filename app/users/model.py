from app.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

'''
import enum
from sqlalchemy import Enum

class Role(enum.Enum):
'''

    

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(120), unique=True)
    emailVerified = db.Column(db.Boolean, default=False, nullable=False)
    isAuthor = db.Column(db.Boolean, default=False, nullable=False)
    isAdmin = db.Column(db.Boolean, default=False, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    