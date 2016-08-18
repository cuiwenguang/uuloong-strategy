# This file test_campigns is created by lincan for Project uuloong-strategy
# on a date of 8/17/16 - 3:01 PM

import unittest
from flask import json
from mongoengine import connect
from manage import app

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"

UniversalHeader = {
    "Content-Type": "application/json"
}


class CampaignsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db = connect('uuloong-strategy')
        db.drop_database('uuloong-strategy')

    def test_post_campaigns(self):
        sample_campaigns = {
            "name": "ChartBoost_1",
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["name"], "ChartBoost_1", "campaigns name should be 'ChartBoost_1'. but got " + str(data["name"]))
        self.assertEqual(data["supplier"], "ChartBoost", "campaigns supplier should be 'ChartBoost'. but got " + str(data["name"]))
        self.assertEqual(data["enum"], "kCampaignsChartBoost", "campaigns enum should be 'kCampaignsChartBoost'. but got " + str(data["name"]))
        self.assertNotEqual(data["id"], "", "id should not be empty")

    def test_get_campaigns(self):
        sample_campaigns = {
            "name": "ChartBoost_1",
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        rv = self.app.get('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data[0]["id"], "since database only have one entry, get game should be same as saved one")

        sample_campaigns = {
            "name": "ChartBoost_2",
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        # get two games
        rv = self.app.get('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(len(data), 2, "database should have two entry")

        # get specific game
        rv = self.app.get('/api/v1.0/campaigns/' + game_id, data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data["id"], "id should be campaigns as the first one")

    def test_put_campaigns(self):
        sample_campaigns = {
            "name": "ChartBoost_1",
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        sample_campaigns = {
            "name": "ChartBoost_2",
            "supplier": "Admob",
            "access_info": {
                "key": "fadsfadfafdasf"
            },
            "enum": "kCampaignsAdmob"
        }

        rv = self.app.put('/api/v1.0/campaigns/' + game_id, data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        self.assertEqual(data["name"], "ChartBoost_2", "campaigns name had changed to 'ChartBoost_2'")
        self.assertEqual(data["supplier"], "Admob", "campaigns supplier had changed to 'Admob'")
        self.assertEqual(data["enum"], "kCampaignsAdmob", "campaigns enum had changed to 'kCampaignsAdmob'")
        self.assertEqual(data["access_info"]["key"], "fadsfadfafdasf", "campaigns access_info -> key had changed to 'fadsfadfafdasf'")

    def test_delete_campaigns(self):
        sample_campaigns = {
            "name": "ChartBoost_1",
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        rv = self.app.delete('/api/v1.0/campaigns/' + game_id, data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        # try to get this game
        rv = self.app.get('/api/v1.0/campaigns/' + game_id, data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create campaigns should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data.get("id"), None, "id should be same as the first one")
