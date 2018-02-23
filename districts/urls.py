from django.conf.urls import url
from districts import views as district_views


urlpatterns = [
    url(r'^$', district_views.DistrictList.as_view()),
    url(r'^(?P<ward>[0-9]+)/$',
        district_views.DistrictDetail.as_view()),
]
