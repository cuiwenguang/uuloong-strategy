# encoding:utf-8
from marshmallow_mongoengine import ModelSchema
from marshmallow import post_dump, pre_load
from ..models.series_data import SeriesData


class SeriesDataSchema(ModelSchema):
    class Meta:
        model = SeriesData

    @post_dump
    def post_dump_process(self, data):
        # 提交验证，业务不清楚，改部分代码暂时不加, cui
        return data

series_datum_schema = SeriesDataSchema()
series_data_schema = SeriesDataSchema(many=True)

