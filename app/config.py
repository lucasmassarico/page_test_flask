import os

class Config:
    FLASK_ADMIN_SWATCH = "flatly"
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]

    # for development
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["DATABASE_TRACK_MODIFICATIONS"]
    TESTING = True
