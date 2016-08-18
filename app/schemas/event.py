from marshmallow_mongoengine import ModelSchema
from marshmallow import post_dump, pre_load
from ..models.event import Event
from ..models.game import Game


class EventSchema(ModelSchema):
    class Meta:
        model = Event

    @pre_load
    def pre_load_process(self, data):
        game_id = data.get("game_id")
        if game_id is None:
            return data

        game = Game.objects(id=game_id).first()
        if game is None:
            raise ValueError("input game id does not exits on system")

        return data

    @post_dump
    def post_dump_process(self, data):
        game_id = data.get("game_id")
        if game_id is None:
            return data

        game = Game.objects(id=game_id).first()
        game.ios_access_key = None
        game.android_access_key = None

        del data["game_id"]
        # need better way to serializer game
        data["game"] = {
            "name": game.name
        }

        return data


event_schema = EventSchema()
events_schema = EventSchema(many=True)
