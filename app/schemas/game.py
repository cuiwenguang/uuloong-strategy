from marshmallow_mongoengine import ModelSchema
from ..models.game import Game


class GameSchema(ModelSchema):

    class Meta:
        model = Game


game_schema = GameSchema()
games_schema = GameSchema(many=True)
