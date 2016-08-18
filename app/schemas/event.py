from marshmallow_mongoengine import ModelSchema
from marshmallow import post_dump
from ..models.event import Event
from ..models.game import Game


class EventSchema(ModelSchema):
    class Meta:
        model = Event

    @post_dump
    def post_dump_process(self, data):
        game_id = data.get("game_id")
        if game_id is None:
            return data

        game = Game.objects.get(id=game_id)
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
