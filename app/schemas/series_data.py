from .. import ma
from ..models.series_data import SeriesData


class SeriesDataSchema(ma.Schema):

    class Meta:
        fields = ('id')


series_datum_schema = SeriesDataSchema()
series_data_schema = SeriesDataSchema(many=True)
