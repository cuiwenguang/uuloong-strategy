from flask import Blueprint

api = Blueprint('api_v1_0', __name__)

# Import any endpoints here to make them available
# from . import dis_endpoint, dat_endpoint
from app.api_v1_0 import strategy
