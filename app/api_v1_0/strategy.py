from flask import request, Response, jsonify

from . import api
from ..models.strategy import Strategy
from ..schemas.strategy import strategy_schema, strategies_schema


class ServerException(Exception):
    def to_dict(self):
        rv = {
            'message': self.message,
        }
        return rv


@api.route('/strategy', methods=['GET'])
def get_strategies():
    try:
        strategy = Strategy.get_first()
        data = strategy_schema.dump(strategy).data

    except Exception as e:
        print "ServerException " + e.message
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/strategy', methods=['PUT'])
def update_strategy():
    try:
        content = request.json
        strategy = strategy_schema.load(content).data
        Strategy.upsert(strategy)

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(content)


@api.errorhandler(ServerException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = 500
    return response
