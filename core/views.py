import json

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class ContactsSPAView(LoginRequiredMixin, View):
    """
    Renders initial page for Vue.js contacts SPA
    """

    def get(self, request, *args, **kwargs):
        context = {}  # TODO pass initial data
        return render(request, 'core/home.html', context=context)
