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
    """
    see https://stackoverflow.com/questions/28799117/error-in-django-test-using-factory-boy
    and http://factoryboy.readthedocs.io/en/latest/recipes.html#simple-many-to-many-relationship
    """
    class Meta:
        model = Contact

    @factory.post_generation
    def addresses(self, create, extracted, **kwargs):

        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for address in extracted:
                self.addresses.add(address)

    @factory.post_generation
    def emails(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for email in extracted:
                self.emails.add(email)

    @factory.post_generation
    def phones(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for phone in extracted:
                self.phones.add(phone)
