from django.conf.urls import url

from core.views import HomeView, DetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^detail$', DetailView.as_view(), name='detail'),
]
