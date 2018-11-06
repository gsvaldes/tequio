"""
API views for Contact and related models
"""
from rest_framework import viewsets

from contacts.models import Contact, Address, Phone, Email, Tag, Note
from contacts.serializers import ContactSerializer, UserSerializer, \
    AddressSerializer, PhoneSerializer, EmailSerializer, TagSerializer, \
    NoteSerializer
from users.models import TequioUser


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


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
