import factory

from users.models import TequioUser


class TequioUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = TequioUser
