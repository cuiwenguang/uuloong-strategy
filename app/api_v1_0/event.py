from flask import jsonify, request

from . import api
from .exception import ServerException
from ..models.event import Event
from ..schemas.event import event_schema, events_schema


@api.route('/events', methods=['GET'])
def get_events():
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        events = Event.objects(game_id=game_id)
        data = events_schema.dump(events).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/events/<string:id>', methods=['GET'])
def get_event(id):
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        event = Event.objects(id=id).first()
        data = event_schema.dump(event).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/events', methods=['POST'])
def create_event():
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        content = request.json

        event = event_schema.load(content).data
        event.game_id = game_id

        if Event.get_first(game_id, event.name) is None:
            event.save()
        else:
            raise ServerException("Object Already Exists")

        data = event_schema.dump(event).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/events/<string:id>', methods=['PUT'])
def update_event(id):
    game_id = request.args.get('game_id')
    if game_id is None:
        raise ServerException("Game Not Found")

    try:
        content = request.json
        a_event = event_schema.load(content).data

        event = Event.objects.get(id=id)
        if event is None:
            raise ServerException("Object Not Found")

        event.name = a_event.name
        event.probability = a_event.probability
        event.save()

        data = event_schema.dump(event).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/events/<string:id>', methods=['DELETE'])
def delete_event(id):
    try:
        event = Event.objects(id=id).first()
        event.delete()

        data = event_schema.dump(event).data
    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)
