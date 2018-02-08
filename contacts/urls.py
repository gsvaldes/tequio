from django.conf.urls import url, include
from rest_framework import routers
from contacts import views


router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'phones', views.PhoneViewSet)
router.register(r'emails', views.EmailViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
