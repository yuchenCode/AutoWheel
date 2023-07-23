from flask import Flask, render_template
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
# moment = Moment()
babel = Babel()
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO(cors_allowed_origins='*')
# login_manager.login_view = 'auth.login'
babel = Babel()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def create_app(cfg_type: str):
    """
    Do initlization for flask application

    :param cfg_type: a string with content ('dev', 'test', 'release')
    :return: app: flask application to run
    """
    app = Flask(__name__)
    app.config.from_object(config[cfg_type])
    config[cfg_type].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .imgSearch import imgSearch as imgSearch_blueprint
    app.register_blueprint(imgSearch_blueprint, url_prefix='/imgSearch')

    from .chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint, url_prefix='/chat')

    return app
