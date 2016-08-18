# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Tactics(EmbeddedDocument):
    mins = FloatField()
    times = FloatField()


class Advertise(EmbeddedDocument):
    campaign_id = StringField()

    tactic = EmbeddedDocumentField(Tactics)
    z_index = IntField()


class Strategy(Document):
    game_id = StringField()

    country = StringField()
    device_model = StringField()

    banner_campaign = ListField(EmbeddedDocumentField(Advertise))
    interstitial_campaign = ListField(EmbeddedDocumentField(Advertise))
    video_campaign = ListField(EmbeddedDocumentField(Advertise))

    def __repr__(self):
        return 'Strategy {}>'.format(self.id)

    @staticmethod
    def get_first(game_id, country, device_model):
        return Strategy.objects(game_id=game_id, country=country, device_model=device_model).first()
