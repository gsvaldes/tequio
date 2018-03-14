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


class DetailView(LoginRequiredMixin, View):
    """
    see and and contact details
    """

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(
            instance=instance, context={'request': request})
        data = json.dumps(serializer.data)
        context = {'data': data}
        return render(request, 'core/detail.html', context=context)


class CreateView(LoginRequiredMixin, View):
    """
    create a new contact
    """

    def get(self, request, *args, **kwargs):
        context = {'data': {'foo': 'bar'}}
        return render(request, 'core/create.html', context=context)


class UpdateView(LoginRequiredMixin, View):
    pass
