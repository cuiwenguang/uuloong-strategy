from marshmallow_mongoengine import ModelSchema
from ..models.strategy import Strategy


class StrategySchema(ModelSchema):

    class Meta:
        model = Strategy


strategy_schema = StrategySchema()
strategies_schema = StrategySchema(many=True)
