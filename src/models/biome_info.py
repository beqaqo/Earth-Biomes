from .base import BaseModel
from src.ext import db

class BiomeInfo(BaseModel):
    __tablename__ = 'biomeinfos'

    category = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    biome_id = db.Column(db.Integer, db.ForeignKey('biomes.id'))

    biome = db.relationship('Biome', back_populates='biome_infos')
    images = db.relationship('Image', back_populates='biome_info')