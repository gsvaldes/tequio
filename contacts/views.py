from django.shortcuts import render
from rest_framework import viewsets
from contacts.models import Contact, Address, Phone, Email
from users.models import TequioUser
from contacts.serializers import ContactSerializer, UserSerializer, \
    AddressSerializer, PhoneSerializer, EmailSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TequioUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer