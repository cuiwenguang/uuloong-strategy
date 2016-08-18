# This file test_event is created by lincan for Project uuloong-strategy
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


class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        # create a game object
        data = self.create_game()
        self.game_id = data["id"]
        self.universal_query_string = {"game_id": self.game_id}

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

    def test_post_event(self):
        sample_event = {
            "name": "test_event",
            "probability": 0.8
        }

        rv = self.app.post('/api/v1.0/events', data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["name"], "test_event", "event name should be 'test_event'. but got " + str(data["name"]))
        self.assertEqual(data["probability"], 0.8, "event probability should be 0.8")

    def test_get_event(self):
        # create_event
        sample_event = {
            "name": "test_event",
            "probability": 0.8
        }

        rv = self.app.post('/api/v1.0/events', data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create event should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        rv = self.app.get('/api/v1.0/events', headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "get event should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data[0]["id"], "since database only have one entry, get game should be same as saved one")

        sample_event = {
            "name": "test_event_2",
            "probability": 1
        }

        rv = self.app.post('/api/v1.0/events', data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create events should return 200. but got " + str(rv.status_code))

        # get two games
        rv = self.app.get('/api/v1.0/events', headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create events should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(len(data), 2, "database should have two entry")

        # get specific game
        rv = self.app.get('/api/v1.0/events/' + game_id, headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create events should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data["id"], "id should be events as the first one")

    def test_put_events(self):
        sample_event = {
            "name": "test_event",
            "probability": 1
        }

        rv = self.app.post('/api/v1.0/events', data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create event should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        event_id = data["id"]

        sample_event = {
            "name": "test_event_23",
            "probability": 0
        }

        rv = self.app.put('/api/v1.0/events/' + event_id, data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create event should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        self.assertEqual(data["name"], "test_event_23", "event name had changed to 'test_event_23'")
        self.assertEqual(data["probability"], 0, "event supplier had changed to 0 , but got " + str(data["probability"]))

        # get this change
        rv = self.app.get('/api/v1.0/events/' + event_id, headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create event should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        self.assertEqual(data["name"], "test_event_23", "event name had changed to 'test_event_23'")
        self.assertEqual(data["probability"], 0, "event supplier had changed to 'probability'")

    def test_delete_events(self):
        sample_event = {
            "name": "test_event",
            "probability": 1
        }

        rv = self.app.post('/api/v1.0/events', data=json.dumps(sample_event), headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "create event should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        event_id = data["id"]

        rv = self.app.delete('/api/v1.0/events/' + event_id, headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "delete event should return 200. but got " + str(rv.status_code))

        # try to get this game
        rv = self.app.get('/api/v1.0/events/' + event_id, headers=UniversalHeader, query_string=self.universal_query_string)
        self.assertEqual(rv.status_code, 200, "get event should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data.get("id"), None, "id should be same as the first one")
