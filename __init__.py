from flask import Flask
# from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from .session_setup import sess
from .frontend import frontend
from .nav import nav
from .model.user import db

def create_app(configfile=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'toto-lea'
    app.config['SESSION_TYPE'] = 'filesystem'

    Bootstrap(app)
    
    

    app.register_blueprint(frontend)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flaskapp'
    nav.init_app(app)
    db.init_app(app)
    sess.init_app(app)
    return app