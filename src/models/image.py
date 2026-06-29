from .base import BaseModel
from src.ext import db

class Image(BaseModel):
    __tablename__ = 'images'

    img = db.Column(db.String)
    order = db.Column(db.Integer)

    biome_info_id = db.Column(db.Integer, db.ForeignKey('biomeinfos.id'))

    biome_info = db.relationship('BiomeInfo', back_populates='images')