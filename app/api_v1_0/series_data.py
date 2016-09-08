import json

from flask import jsonify, request

from . import api
from .exception import ServerException
from ..models.series_data import SeriesData
from ..schemas.series_data import series_datum_schema, series_data_schema

'''
@api.route('/series_data', methods=['GET'])
def get_series_data():
    pass


@api.route('/series_data/<int:id>', methods=['GET'])
def get_series_data(id):
    pass
'''


@api.route('/series_data', methods=['POST'])
def create_series_data():
    try:
        data = series_data_schema.load(request.json).data
        SeriesData.objects.insert(data);
    except Exception as e:
        raise ServerException(e.message)

    return jsonify({"success": True})
