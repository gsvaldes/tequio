from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from contacts.models import Contact

from contacts.serializers import ContactSerializer


NEW_CONTACT = """
{
    "emails": [
        {
            "email": "tierra@libertad.org"
        }
    ],
    "addresses": [
        {
            "address": "123 Ahuizote Avenue",
            "city": "New Haven",
            "state": "CT",
            "zip_code": "06511",
            "country": "USA",
        }
    ],
    "phones": [
        {
            "number": "9995551234",
        }
    ],
    "name": "Ricardo Flores Magon",
    "member": false
}
"""


# class TestContactSerializers(TestCase):
#     """
#     """
#     def test_create_contact(self):
#         """create a new contact from json"""
#         data = ''
