from flask import Blueprint
from ..common.http_auth import HTTPTokenAuth

api = Blueprint('api_v1_0', __name__)
auth = HTTPTokenAuth()

from app.api_v1_0 import authentication

# Import any endpoints here to make them available
# from . import dis_endpoint, dat_endpoint
from app.api_v1_0 import strategy
from app.api_v1_0 import event
from app.api_v1_0 import game
from app.api_v1_0 import campaign
from app.api_v1_0 import series_data
