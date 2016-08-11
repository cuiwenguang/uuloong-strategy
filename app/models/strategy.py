# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *
from bson import json_util

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Strategy(Document):
    banner = ListField(StringField())
    interstitial = ListField(StringField())
    video = ListField(StringField())

    def __repr__(self):
        return 'Strategy {}>'.format(self.id)

    @staticmethod
    def get_first():
        return Strategy.objects.first()

    @staticmethod
    def upsert(strategy):
        first_object = Strategy.get_first()

        if first_object is None:
            strategy.save()
        else:
            if strategy.banner is not None:
                first_object.banner = strategy.banner

            if strategy.interstitial is not None:
                first_object.interstitial = strategy.interstitial

            if strategy.video is not None:
                first_object.video = strategy.video

            first_object.save()
