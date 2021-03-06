"""tequio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView

from core import urls as core_urls
from contacts import urls as contact_urls
from districts import urls as districts_urls

urlpatterns = [
    # TODO add redirect url to home
    url(r'^manage/', include(core_urls)),
    url(r'^contacts/', include(contact_urls)),
    url(r'^districts/', include(districts_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('contacts-spa'))),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
