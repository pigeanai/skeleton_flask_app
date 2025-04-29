from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
from app.controllers.logging import set_up_logging

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "main.main"
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
        
    set_up_logging(app)

    app.logger.info('Launching Flaskapp')

    return app

from .models import User