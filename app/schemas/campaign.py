from marshmallow_mongoengine import ModelSchema
from ..models.campaign import Campaign


class CampaignSchema(ModelSchema):

    class Meta:
        model = Campaign


campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)
