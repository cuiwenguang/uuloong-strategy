# -*- coding: utf-8 -*-
# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *
from bson import ObjectId

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Event(Document):
    """
    Event 用于描述广告触发的时间概略
    """
    game_id = StringField()  # 本概率属于哪一个游戏
    name = StringField()  # 本概率的名词,用于标识用
    probability = FloatField()  # 本概率显示事件,域(0, 1)

    def __repr__(self):
        return 'Event {}>'.format(self.id)

    @staticmethod
    def new(game_id, name, probability):
        event = Event()
        event.game_id = game_id
        event.name = name
        event.probability = probability
        return event

    @staticmethod
    def get_first(game_id, name):
        return Event.objects(game_id=game_id, name=name).first()
