from rest_framework_gis.serializers import GeoFeatureModelSerializer
from districts.models import AlderDistrict


class DistrictSerializer(GeoFeatureModelSerializer):
    """
    Geo Serialize the district model
    """
    class Meta:
        model = AlderDistrict
        geo_field = 'mpoly'

        fields = ('alder', 'wards_txt', 'wards_desc')
