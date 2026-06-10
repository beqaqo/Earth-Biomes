from src.models.base import BaseModel
from src.ext import db

class Biome(BaseModel):
    __tablename__ = 'biomes'

    name = db.Column(db.String, nullable=False)
    location = db.Column(db.Text, nullable=False)
    climate = db.Column(db.Text, nullable=False)
    soil = db.Column(db.Text, nullable=False)
    vegetation = db.Column(db.Text, nullable=False)

    important_plants = db.Column(db.Text, nullable=False)
    biome_icon = db.Column(db.String(64), nullable=False)
    title_img = db.Column(db.String(64), nullable=False)
    distribution_img = db.Column(db.String(64), nullable=False)

    previous_biome = db.Column(db.Integer, db.ForeignKey('biomes.id'), nullable=True)
    next_biome = db.Column(db.Integer, db.ForeignKey('biomes.id'), nullable=True)

