# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Campaign(Document):
    name = StringField()
    supplier = StringField()
    access_info = DictField()
    enum = StringField()

    def __repr__(self):
        return 'Campaign {}>'.format(self.id)

    @staticmethod
    def new(name, supplier, access_info, enum):
        campaign = Campaign()
        campaign.name = name
        campaign.supplier = supplier
        campaign.access_info = access_info
        campaign.enum = enum
        return campaign
