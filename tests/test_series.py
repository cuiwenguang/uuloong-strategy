# This file test_strategy is created by lincan for Project uuloong-strategy
# on a date of 8/17/16 - 3:14 PM

import datetime
import unittest
from flask import json
from mongoengine import connect
from manage import app

__author__ = "cui"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "cui"
__status__ = "Production"

UniversalHeader = {
    "Content-Type": "application/json"
}

class StrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db = connect('uuloong-strategy')
        db.drop_database('uuloong-strategy')

    def test_post_serise(self):
        test_data = [
            {
                "timestamp": datetime.datetime.now(),
                "type": "type_test",
                "Value": {
                    "campaign": "capaign1",
                    "campaign_type": "1",
                    "if_displayed": True,
                    "if_clicked": True,
                    "video_duration": 0.3,
                    "if_download": False,
                    "if_failed": True,
                    "info": "remark"
                }
            },
            {
                "timestamp": datetime.datetime.now(),
                "type": "type_test",
                "Value": {
                    "campaign": "capaign2",
                    "campaign_type": "1",
                    "if_displayed": True,
                    "if_clicked": True,
                    "video_duration": 0.3,
                    "if_download": False,
                    "if_failed": True,
                    "info": "remark"
                }
            }
        ]

        rv = self.app.post('/api/v1.0/series_data', data=json.dumps(test_data), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create serise_data should return 200. but got " + str(rv.status_code))
