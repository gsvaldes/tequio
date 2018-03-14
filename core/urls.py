from django.conf.urls import url

from core.views import HomeView, DetailView, CreateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^create/$', CreateView.as_view(), name='create'),
]
