# -*- coding: utf-8 -*-
# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Tactics(EmbeddedDocument):
    """
    Tactics 描述具体广告提供者的策略
    """
    mins = FloatField()  # 广告每几分钟显示一次
    times = FloatField()  # 广告一共显示几次


class Advertise(EmbeddedDocument):
    """
    Advertise 用于描述具体广告商的策略
    """
    campaign_id = StringField()  # 广告提供者 ID

    tactic = EmbeddedDocumentField(Tactics)  # 具体广告商的策略
    z_index = IntField()  # 广告优先级,按照 1000 往下,降幂


class Strategy(Document):
    """
    Strategy 用于描述广告显示策略
    """
    game_id = StringField()  # Game ID

    country = StringField()  # 策略所属国家,需要按照 ISO 3361 标准
    device_model = StringField()  # 策略所属设备, 可选为 iOS 和 Android

    banner_campaign = ListField(EmbeddedDocumentField(Advertise))  # banner 策略
    interstitial_campaign = ListField(EmbeddedDocumentField(Advertise))  # 插页策略
    video_campaign = ListField(EmbeddedDocumentField(Advertise))  # 视频策略

    def __repr__(self):
        return 'Strategy {}>'.format(self.id)

    @staticmethod
    def get_first(game_id, country, device_model):
        return Strategy.objects(game_id=game_id, country=country, device_model=device_model).first()
