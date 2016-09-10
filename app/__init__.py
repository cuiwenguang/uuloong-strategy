from flask import Flask

from config import config
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config[config_name])
    app.debug = True

    from .api_v1_0 import api as api_v1_0_blueprint
    from .web import web as web_blueprint
    app.register_blueprint(api_v1_0_blueprint, url_prefix='/api/v1.0')
    app.register_blueprint(web_blueprint, url_prefix='/')
    return app
