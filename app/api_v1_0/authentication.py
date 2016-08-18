# This file authentication is created by lincan for Project uuloong-strategy
# on a date of 8/15/16 - 1:51 PM

from . import auth
from ..models.game import Game
from .exception import ServerException
from flask import g, jsonify
from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


@auth.verify_app_id
def verify_token(token):
    if token == '':
        return False

    query = Game.objects(Q(ios_access_key=token) or Q(android_access_key=token))
    game = query.first()

    if game is None:
        return False

    g.game = game

    if game.ios_access_key == token:
        g.game_mode = 'iOS'
    else:
        g.game_mode = 'Android'

    return True


@auth.verify_token
def verify_token(token):
    if token == '':
        return False

    return True


@auth.error_handler
def auth_error():
    return ServerException('Invalid credentials')
