"""
model factories used for creating testing instances
of Contact and related models
see http://factoryboy.readthedocs.io/
"""
import factory

from contacts.models import Address, Phone, Email, Contact


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address


class PhoneFactory(factory.DjangoModelFactory):
    class Meta:
        model = Phone


class EmailFactory(factory.DjangoModelFactory):
    class Meta:
        model = Email


class ContactFactory(factory.DjangoModelFactory):
    class Meta:
        model = Contact
