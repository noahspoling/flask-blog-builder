import os

class Config:
    SECRET_KEY = 'my-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'