from django.conf.urls import url

from core.views import ContactsSPAView

urlpatterns = [
    url(r'^$', ContactsSPAView.as_view(), name='contacts-spa'),
]
