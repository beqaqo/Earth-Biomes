from src.models.base import BaseModel
from src.ext import db
from flask_login import UserMixin

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)