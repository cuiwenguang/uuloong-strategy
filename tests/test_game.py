# This file game.py is created by lincan for Project uuloong-strategy
# on a date of 8/17/16 - 2:18 PM

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


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db = connect('uuloong-strategy')
        db.drop_database('uuloong-strategy')

    def test_post_game(self):
        sample_game = {
            "name": "puzzle_game"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data["name"], "puzzle_game", "game name should be 'puzzle_game'. but got " + str(data["name"]))
        self.assertNotEqual(data["id"], "", "id should not be empty")

    def test_get_game(self):
        sample_game = {
            "name": "puzzle_game_1"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        rv = self.app.get('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data[0]["id"], "since database only have one entry, get game should be same as saved one")

        sample_game = {
            "name": "puzzle_game_2"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        # get two games
        rv = self.app.get('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(len(data), 2, "database should have two entry")

        # get specific game
        rv = self.app.get('/api/v1.0/games/' + game_id, data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(game_id, data["id"], "id should be same as the first one")

    def test_put_game(self):
        sample_game = {
            "name": "puzzle_game_1"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        sample_game = {
            "name": "puzzle_game_5"
        }

        rv = self.app.put('/api/v1.0/games/' + game_id, data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        self.assertEqual(data["name"], "puzzle_game_5", "game name had changed to 'puzzle_game_5'")

    def test_delete_game(self):
        sample_game = {
            "name": "puzzle_game_1"
        }

        rv = self.app.post('/api/v1.0/games', data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))
        data = json.loads(rv.data)

        game_id = data["id"]

        rv = self.app.delete('/api/v1.0/games/' + game_id, data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        # try to get this game
        rv = self.app.get('/api/v1.0/games/' + game_id, data=json.dumps(sample_game), headers=UniversalHeader)
        self.assertEqual(rv.status_code, 200, "create game should return 200. but got " + str(rv.status_code))

        data = json.loads(rv.data)
        self.assertEqual(data.get("id"), None, "id should be same as the first one")


if __name__ == '__main__':
    unittest.main()
