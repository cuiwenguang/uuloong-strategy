# -*- coding: utf-8 -*-
# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/15/16 - 10:56 AM

from mongoengine import *
import string
import random

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Game(Document):
    """
    Game 用于描述游戏对象
    """
    name = StringField()  # Game 名称
    ios_access_key = StringField()  # iOS 访问服务器时所需要的 key
    android_access_key = StringField()  # Android 访问服务器所需要的 key

    def __repr__(self):
        return 'Game {}>'.format(self.id)

    @staticmethod
    def new(name):
        """
        创建一个新的游戏
        :param name:
        :return:
        """
        game = Game()
        game.name = name
        game.ios_access_key = random_string_generator(32)
        game.android_access_key = random_string_generator(32)
        return game

    @staticmethod
    def get_first(name):
        return Game.objects(name=name)
