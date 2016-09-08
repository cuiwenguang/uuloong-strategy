# -*- coding: utf-8 -*-
# This file strategy.py is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 10:56 AM

from mongoengine import *

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"


class Campaign(Document):
    """
    Campaign 用于描述具体的广告提供者对象, 广告商对象可以用于描述同一广告商的多个账号
    """
    name = StringField()  # 名称
    supplier = StringField()  # 广告商名称
    access_info = DictField()  # 广告提供者访问信息
    enum = StringField()  # 广告提供者对象的key, 用于和客户端沟通用, 本字段所保存的对象需要谨慎填写

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
