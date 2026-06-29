from src.models.base import BaseModel
from src.ext import db

class Question(BaseModel):
    __tablename__ = 'questions'

    question = db.Column(db.String(255), nullable=False)
    a = db.Column(db.String(256), nullable=False)
    b = db.Column(db.String(256), nullable=False)
    c = db.Column(db.String(256), nullable=False)
    d = db.Column(db.String(256), nullable=False)
    correct = db.Column(db.String(1))
