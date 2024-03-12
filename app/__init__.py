from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData 
from config import config
from flask_login import LoginManager

db = SQLAlchemy(metadata=MetaData(naming_convention={
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
}))
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    #register the main blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #register the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
