import os
from django.contrib.gis.utils import LayerMapping
from districts.models import AlderDistrict


DISTRICT_MAPPING = {
    'shape_area': 'shape_area',
    'wards_desc': 'wards_desc',
    'alder': 'alder',
    'lci_ward_g': 'lci_ward_g',
    'shape_length': 'shape_len',
    'wards': 'wards',
    'wards_txt': 'warrds_txt',  # note extra r in original data source
    'mpoly': 'POLYGON',
}


DISTRICT_SHP = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 'data',
                 'district.shp'),
)


def run(verbose=True):
    """
    load data from shp files to AlderDistrict table
    to reload data, rename shp files in format
    district.dbf
    district.prj
    district.shp
    district.shx
    """
    lm = LayerMapping(
        AlderDistrict, DISTRICT_SHP, DISTRICT_MAPPING,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
