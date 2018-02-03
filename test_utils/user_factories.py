"""
model factories used for creating testing instances
of User model
see http://factoryboy.readthedocs.io/
"""
import factory

from users.models import TequioUser


class TequioUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = TequioUser
