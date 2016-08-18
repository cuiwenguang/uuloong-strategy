from flask import request, Response, jsonify, g

from . import api, auth
from .exception import ServerException
from ..models.strategy import Strategy
from ..schemas.strategy import strategy_schema, strategies_schema
from ..common.device_model import DeviceModel
from ..common.geo_location import GeoLocation


@api.route('/strategy', methods=['GET'])
@auth.app_auth_required
def get_strategy():
    try:
        game_id = str(g.game.id)
        phone_model = g.game_mode

        client_location = GeoLocation(request.remote_addr)
        strategy = Strategy.get_first(game_id, client_location.location, phone_model)

        data = strategy_schema.dump(strategy).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/strategies', methods=['GET'])
# @auth.user_login_required
def get_strategies():
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        # phone_model = request.args.get('phone_model')
        # client_country = request.args.get('country_code')
        # query = {
        #     "game_id": game_id
        # }

        # if phone_model is not None:
        #     model = DeviceModel(phone_model)
        #     query["device_model"] = model.enum
        #
        # if client_country is not None:
        #     query["country"] = client_country

        strategy = Strategy.objects(game_id=game_id)
        data = strategies_schema.dump(strategy).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/strategies/<string:id>', methods=['GET'])
# @auth.user_login_required
def get_strategies_id(id):
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        strategy = Strategy.objects(id=id).first()
        data = strategy_schema.dump(strategy).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/strategies', methods=['POST'])
def create_strategy():
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        content = request.json
        strategy = strategy_schema.load(content).data

        if Strategy.get_first(strategy.game_id, strategy.country, strategy.device_model) is not None:
            raise ServerException("Object Already Exists")

        strategy.save()
        data = strategy_schema.dump(strategy).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/strategies/<string:id>', methods=['PUT'])
# @auth.user_login_required
def update_strategy(id):
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        content = request.json
        a_strategy = strategy_schema.load(content).data

        strategy = Strategy.objects.get(id=id)
        if strategy is None:
            raise ServerException("Object Not Found")

        if strategy.banner_campaign is not None:
            strategy.banner_campaign = a_strategy.banner_campaign

        if strategy.interstitial_campaign is not None:
            strategy.interstitial_campaign = a_strategy.interstitial_campaign

        if strategy.video_campaign is not None:
            strategy.video_campaign = a_strategy.video_campaign

        strategy.save()

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(content)


@api.route('/strategies/<string:id>', methods=['DELETE'])
def delete_strategy(id):
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        strategy = Strategy.objects(id=id)
        strategy.delete()

        data = strategy_schema.dump(strategy).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)
