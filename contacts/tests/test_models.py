from django.test import TestCase

from contacts.models import Address


class TestAddressModel(TestCase):
    def test_address_string_method(self):
        """
        __str__ should return
        {address}-{city}-{state}-{zip}
        """
        address = Address.objects.create(
            address='123 Ahuizote Avenue',
            city='Etla',
            state='Kansas',
            zip_code='12345'
        )
        self.assertEqual(
            address.__str__(),
            '123 Ahuizote Avenue-Etla-Kansas-12345'
        )
