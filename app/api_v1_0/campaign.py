from flask import jsonify, request

from . import api
from .exception import ServerException
from ..models.campaign import Campaign
from ..schemas.campaign import campaign_schema, campaigns_schema


@api.route('/campaigns', methods=['GET'])
def get_campaigns():
    try:
        campaigns = Campaign.objects
        data = campaigns_schema.dump(campaigns).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/campaigns/<string:id>', methods=['GET'])
def get_campaign(id):
    try:
        campaigns = Campaign.objects(id=id).first()
        data = campaign_schema.dump(campaigns).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/campaigns', methods=['POST'])
def create_campaign():
    try:
        content = request.json
        campaign = campaign_schema.load(content).data

        if Campaign.objects(name=campaign.name).first() is not None:
            raise ServerException("Object Name Already Exists")

        campaign.save()
        data = campaign_schema.dump(campaign).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/campaigns/<string:id>', methods=['PUT'])
def update_campaign(id):
    try:
        content = request.json
        a_campaign = campaign_schema.load(content).data

        campaign = Campaign.objects.get(id=id)
        if campaign is None:
            raise ServerException("Object Not Found")

        campaign.name = a_campaign.name
        campaign.supplier = a_campaign.supplier
        campaign.access_info = a_campaign.access_info
        campaign.enum = a_campaign.enum
        campaign.save()

        data = campaign_schema.dump(campaign).data

    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)


@api.route('/campaigns/<string:id>', methods=['DELETE'])
def delete_campaign(id):
    try:
        campaign = Campaign.objects(id=id).first()
        campaign.delete()
        data = campaign_schema.dump(campaign).data
    except Exception as e:
        raise ServerException(e.message)

    return jsonify(data)
