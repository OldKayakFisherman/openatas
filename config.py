import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET.KEY")
    SQL_ALCHEMY_TRACK_MODIFICATION = False

    def init_app(app):
        pass

class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data-dev.sqlite'

class TestingConfig(Config):

    TESTING = True   
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProductionConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DB.URI")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
