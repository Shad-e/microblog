"""
Factory for application
"""

import logging
from flask import Flask
from flask.logging import default_handler

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap

from prometheus_flask_exporter.multiprocess import (
    GunicornInternalPrometheusMetrics
)

from app.config import ProdConfig, RequestFormatter

# Extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_class=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ✅ CORRECT METRICS INITIALIZATION
    GunicornInternalPrometheusMetrics(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        formatter = RequestFormatter(
            "[%(asctime)s %(levelname)s] %(remote_addr)s requested %(url)s\n"
            ": %(message)s [in %(module)s:%(lineno)d]"
        )
        default_handler.setFormatter(formatter)
        app.logger.setLevel(logging.INFO)

    return app

from app import models  # noqa
