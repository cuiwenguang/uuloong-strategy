from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    app.debug = True

    from .api_v1_0 import api as api_v1_0_blueprint
    app.register_blueprint(api_v1_0_blueprint, url_prefix='/api/v1.0')

    return app