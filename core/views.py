import json

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class HomeView(LoginRequiredMixin, View):
    """
    holding view
    """

    def get(self, request, *args, **kwargs):
        context = {}  # TODO pass initial data
        return render(request, 'core/home.html', context=context)
