from marshmallow_mongoengine import ModelSchema
from marshmallow import post_dump
from ..models.strategy import Strategy
from ..models.campaign import Campaign


class StrategySchema(ModelSchema):
    class Meta:
        model = Strategy

    @post_dump
    def post_dump_process(self, data):
        banner_campaigns = data.get("banner_campaign")
        if banner_campaigns is None:
            banner_campaigns = []

        interstitial_campaigns = data.get("interstitial_campaign")
        if interstitial_campaigns is None:
            interstitial_campaigns = []

        video_campaigns = data.get("video_campaign")
        if video_campaigns is None:
            video_campaigns = []

        all_campaigns = banner_campaigns + interstitial_campaigns + video_campaigns

        campaign_ids = []
        for campaign in all_campaigns:
            campaign_ids.append(campaign.get("campaign_id"))

        campaigns = Campaign.objects(id__in=campaign_ids)
        campaigns_dict = {}

        for campaign in campaigns:
            campaigns_dict[str(campaign.id)] = campaign

        for compaign in all_campaigns:
            campaign_id = compaign.get("campaign_id")
            compaign["campaign"] = campaigns_dict[campaign_id].enum

        return data


strategy_schema = StrategySchema()
strategies_schema = StrategySchema(many=True)
