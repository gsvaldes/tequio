from districts.models import AlderDistrict
from districts.serializers import DistrictSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DistrictList(APIView):
    """
    retrieve all districts
    """

    def get(self, request):
        districts = AlderDistrict.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


class DistrictDetail(APIView):
    """
    retrieve a single district.
    """

    def get_object(self, ward):
        try:
            return AlderDistrict.objects.get(wards=ward)
        except AlderDistrict.DoesNotExist:
            raise Http404

    def get(self, request, ward):
        district = self.get_object(ward)
        serializer = DistrictSerializer(district)
        return Response(serializer.data)
