# encoding:utf-8
# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

import time
from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class SeriesDataType:
    SeriesDataTypeAdsStats = 0


class SeriesDataADsDisplayType:
    SeriesDataTypeADDisplayTypeBanner = 0
    SeriesDataTypeADDisplayTypeInterstitial = 1
    SeriesDataTypeADDisplayTypeVideo = 2


class SeriesDataValue(EmbeddedDocument):
    campaign = StringField()
    campaign_type = StringField()  # SeriesDataADsDisplayType
    if_displayed = BooleanField()
    if_clicked = BooleanField()
    video_duration = FloatField()
    if_download = BooleanField()
    if_failed = BooleanField() # 是否发生错误
    info = StringField() # 备用字段，如果发生错误，这里写简要信息


class SeriesData(Document):
    timestamp = DateTimeField()
    type = StringField()  # SeriesDataType
    Value = EmbeddedDocumentField(SeriesDataValue)

    def __repr__(self):
        return 'SeriesData {}>'.format(self.id)

    @staticmethod
    def get_first(time, type):
        return SeriesData.objects(timestamp=time, type=type).first()
