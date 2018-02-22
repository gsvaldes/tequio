from django.contrib.gis import admin
from districts.models import AlderDistrict


admin.site.register(AlderDistrict, admin.GeoModelAdmin)
