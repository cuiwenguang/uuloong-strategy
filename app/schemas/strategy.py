from marshmallow_mongoengine import ModelSchema
from marshmallow import post_dump, pre_load
from ..models.strategy import Strategy
from ..models.campaign import Campaign
from ..models.game import Game


class StrategySchema(ModelSchema):
    class Meta:
        model = Strategy

    @pre_load
    def pre_load_process(self, data):
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

        if len(campaigns_dict) != len(campaign_ids):
            raise ValueError("input campaigns id does not exits on system")

        game_id = data.get("game_id")
        if game_id is None:
            return data

        game = Game.objects(id=game_id).first()
        if game is None:
            raise ValueError("input game id does not exits on system")

        return data

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

        for campaign in all_campaigns:
            campaign_id = campaign.get("campaign_id")

            campaign_object = campaigns_dict.get(campaign_id)
            campaign["campaign"] = campaign_object.enum if campaign_object is not None else None

        return data


strategy_schema = StrategySchema()
strategies_schema = StrategySchema(many=True)
