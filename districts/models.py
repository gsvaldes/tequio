from django.contrib.gis.db import models as geomodels


class AlderDistrict(geomodels.Model):
    """
    New Haven specific alder ward geo information
    Data Source
    https://data.ct.gov/Government/City-of-New-Haven-Aldermanic-Wards/nki6-723a/data
    """
    shape_area = geomodels.IntegerField()
    wards_desc = geomodels.CharField(max_length=50)
    # TODO should alder just be a CharField, as it is in original data
    # or be ForeignKey to new Alder model
    alder = geomodels.CharField(max_length=100)
    lci_ward_g = geomodels.CharField(max_length=50)
    shape_length = geomodels.IntegerField()
    wards = geomodels.IntegerField()
    wards_txt = geomodels.CharField(max_length=2)

    mpoly = geomodels.MultiPolygonField()

    class Meta:
        ordering = ('wards',)

    def __str__(self):
        return '{0}-{1}'.format(self.wards_desc, self.alder)
