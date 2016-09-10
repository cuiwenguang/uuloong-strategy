from flask import jsonify, request

from . import api
from .exception import ServerException
from ..models.game import Game
from ..schemas.game import game_schema, games_schema




@api.route('/games', methods=['GET'])
def get_games():
    try:
        games = Game.objects
        data = games_schema.dump(games).data
    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/games/<string:id>', methods=['GET'])
def get_game(id):
    try:
        game = Game.objects(id=id).first()
        data = game_schema.dump(game).data
    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/games', methods=['POST'])
def create_game():
    try:
        content = request.json
        game_name = content.get("name")
        if game_name is None:
            raise ServerException("Game Name Requested")

        game = Game.new(game_name)

        if Game.objects(name=game.name).first() is not None:
            raise ServerException("Object Already Exists")

        game.save()

        data = game_schema.dump(game).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/games/<string:id>', methods=['PUT'])
def update_game(id):
    try:
        content = request.json
        agame = game_schema.load(content).data

        game = Game.objects(id=id).first()
        if game is None:
            raise ServerException("Object Not Found")

        game.name = agame.name
        game.save()

        data = game_schema.dump(game).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/games/<string:id>', methods=['DELETE'])
def delete_game(id):
    try:
        game = Game.objects(id=id).first()
        game.delete()

        data = game_schema.dump(game).data
    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)
