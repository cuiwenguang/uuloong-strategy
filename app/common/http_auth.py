# This file http_auth is created by lincan for Project uuloong-strategy
# on a date of 8/15/16 - 2:52 PM

from functools import wraps
from flask import request, make_response

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class HTTPAuth(object):
    def __init__(self):
        def default_get_password(username):
            return None

        def default_auth_error():
            return "Unauthorized Access"

        self.realm = "Authentication Required"
        self.get_password(default_get_password)
        self.error_handler(default_auth_error)

    def get_password(self, f):
        self.get_password_callback = f
        return f

    def error_handler(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            res = f(*args, **kwargs)
            if type(res) == str:
                res = make_response(res)
                res.status_code = 401
            if 'WWW-Authenticate' not in res.headers.keys():
                res.headers['WWW-Authenticate'] = self.authenticate_header()
            return res

        self.auth_error_callback = decorated
        return decorated

    def user_login_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get("X-BYGame-Manager-Token")

            if request.method != 'OPTIONS':
                if not token or not self.authenticate_token(token):
                    return self.auth_error_callback()
            return f(*args, **kwargs)

        return decorated

    def app_auth_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get("X-BYGame-Application-Token")

            if request.method != 'OPTIONS':
                if not token or not self.authenticate_app_id(token):
                    return self.auth_error_callback()
            return f(*args, **kwargs)

        return decorated

    def username(self):
        if not request.authorization:
            return ""
        return request.authorization.username


class HTTPTokenAuth(HTTPAuth):
    def __init__(self):
        super(HTTPTokenAuth, self).__init__()
        self.hash_password(None)
        self.verify_token(None)

    def hash_password(self, f):
        self.hash_password_callback = f
        return f

    def verify_token(self, f):
        self.verify_token_callback = f
        return f

    def verify_app_id(self, f):
        self.verify_app_id_callback = f
        return f

    def authenticate_header(self):
        return 'Basic realm="{0}"'.format(self.realm)

    def authenticate_token(self, token):
        if not token:
            return False

        if self.verify_token_callback:
            return self.verify_token_callback(token)

        return False

    def authenticate_app_id(self, token):
        if not token:
            return False

        if self.verify_app_id_callback:
            return self.verify_app_id_callback(token)

        return False
