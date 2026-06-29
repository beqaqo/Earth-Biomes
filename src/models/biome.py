from src.models.base import BaseModel
from src.ext import db

class Biome(BaseModel):
    __tablename__ = 'biomes'

    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    biome_icon = db.Column(db.String(64), nullable=False)
    title_img = db.Column(db.String(64), nullable=False)
    distribution_img = db.Column(db.String(64), nullable=False)

    previous_biome = db.Column(db.Integer, db.ForeignKey('biomes.id'), nullable=True)
    next_biome = db.Column(db.Integer, db.ForeignKey('biomes.id'), nullable=True)

    biome_infos = db.relationship('BiomeInfo', back_populates='biome')

    def __repr__(self):
        return f'{self.name}'