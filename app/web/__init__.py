from flask import Blueprint

web = Blueprint('web', __name__, static_folder='static')

from app.web import dashboard
