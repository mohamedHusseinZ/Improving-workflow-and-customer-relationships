# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///workflow_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'zaki_jwt_secret_key'  # Change this to a strong key
