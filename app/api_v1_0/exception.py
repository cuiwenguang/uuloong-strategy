# This file exception is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 1:58 PM

from flask import jsonify

from . import api

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class ServerException(Exception):
    def to_dict(self):
        rv = {
            'message': self.message,
        }
        return rv


@api.errorhandler(ServerException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = 500
    return response
