import os

class Config:
    SECRET_KEY = 'SEMOIB1010HTREA'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')