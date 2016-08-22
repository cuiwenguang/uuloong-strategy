# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

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
    campaign = IntField()
    campaign_type = IntField()  # SeriesDataADsDisplayType

    if_displayed = BooleanField()
    if_clicked = BooleanField()
    video_duration = FloatField()
    if_download = BooleanField()


class SeriesData(Document):
    timestamp = DateTimeField()
    type = StringField()  # SeriesDataType
    Value = EmbeddedDocumentField(SeriesDataValue)

    def __repr__(self):
        return 'SeriesData {}>'.format(self.id)
