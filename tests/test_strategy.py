# This file test_strategy is created by lincan for Project uuloong-strategy
# on a date of 8/17/16 - 3:14 PM

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

DefaultQueryString = {
    "country_code": "CN",
    "phone_model": "iOS"
}


class StrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        # create a game object
        data = self.create_game()
        self.game_id = str(data["id"])
        self.game_ios_key = data["ios_access_key"]

        self.post_header = UniversalHeader
        self.post_header["X-BYGame-Application-Token"] = self.game_ios_key

        self.universal_query_string = DefaultQueryString
        self.universal_query_string["game_id"] = self.game_id

    def tearDown(self):
        db = connect('uuloong-strategy')
        db.drop_database('uuloong-strategy')

    def create_game(self):
        sample_game = {
            "name": "puzzle_game"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["name"], "puzzle_game", "game name should be 'puzzle_game'. but got " + str(data["name"]))
        self.assertNotEqual(data["id"], "", "id should not be empty")

        return data

    def create_campaign(self, name):
        sample_campaigns = {
            "name": name,
            "supplier": "ChartBoost",
            "access_info": {
                "key": "13213123213123"
            },
            "enum": "kCampaignsChartBoost"
        }

        rv = self.app.post('/api/v1.0/campaigns', data=json.dumps(sample_campaigns), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["name"], name, "campaigns name should be 'ChartBoost_1'. but got " + str(data["name"]))
        self.assertEqual(data["supplier"], "ChartBoost", "campaigns supplier should be 'ChartBoost'. but got " + str(data["name"]))
        self.assertEqual(data["enum"], "kCampaignsChartBoost", "campaigns enum should be 'kCampaignsChartBoost'. but got " + str(data["name"]))
        self.assertNotEqual(data["id"], "", "id should not be empty")

        return data

    def test_post_event(self):
        c1 = self.create_campaign("name1")
        c2 = self.create_campaign("name2")

        sample_strategy = {
            "game_id": self.game_id,
            "country": "CN",
            "device_model": "iOS",
            "banner_campaign": [{
                "campaign_id": c1["id"],
                "tactic": {
                    "mins": 10
                },
                "z_index": 1000
            }],
            "interstitial_campaign": [{
                "campaign_id": c2["id"],
                "tactic": {
                    "times": 10
                },
                "z_index": 1000
            }],
        }

        rv = self.app.post('/api/v1.0/strategies', data=json.dumps(sample_strategy), headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create strategy should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["game_id"], self.game_id, "event name should be 'test_event'. but got " + str(data["game_id"]))
        self.assertEqual(data["country"], "CN", "event probability should be 0.8")
        self.assertEqual(data["device_model"], "iOS", "event probability should be 0.8")

    def test_get_event(self):
        c1 = self.create_campaign("name1")
        c2 = self.create_campaign("name2")

        sample_strategy = {
            "game_id": self.game_id,
            "country": "CN",
            "device_model": "iOS",
            "banner_campaign": [{
                "campaign_id": c1["id"],
                "tactic": {
                    "mins": 10
                },
                "z_index": 1000
            }],
            "interstitial_campaign": [{
                "campaign_id": c2["id"],
                "tactic": {
                    "times": 10
                },
                "z_index": 1000
            }],
        }

        rv = self.app.post('/api/v1.0/strategies', data=json.dumps(sample_strategy), headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create strategy should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)
        strategy_id = data["id"]

        rv = self.app.get('/api/v1.0/strategies', headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "get strategy should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(len(data), 1, "database now have one entry, but got " + str(len(data)))
        self.assertEqual(strategy_id, data[0]["id"], "since database only have one entry, get game should be same as saved one, but got {0}, {1}".format(strategy_id, data[0]["id"]))

        sample_strategy = {
            "game_id": self.game_id,
            "country": "US",
            "device_model": "iOS",
            "banner_campaign": [{
                "campaign_id": c1["id"],
                "tactic": {
                    "mins": 10
                },
                "z_index": 1000
            }],
            "interstitial_campaign": [{
                "campaign_id": c2["id"],
                "tactic": {
                    "times": 10
                },
                "z_index": 1000
            }],
        }

        rv = self.app.post('/api/v1.0/strategies', data=json.dumps(sample_strategy), headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create strategies should return 200. but got " + str(rv.status_code))

        # get two games
        rv = self.app.get('/api/v1.0/strategies', headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create strategies should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)
        self.assertEqual(len(data), 2, "database should have two entry")

        # get specific game
        rv = self.app.get('/api/v1.0/strategies/' + strategy_id, headers=self.post_header, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "get strategy should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)
        self.assertEqual(strategy_id, data["id"], "id should be events as the first one, but got " + str(data["id"]))
