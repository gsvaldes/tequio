from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from test_utils.user_factories import TequioUserFactory
from contacts.models import Contact


NEW_CONTACT_DATA = {
    "emails": [
        {
            "email": "tierra@libertad.org"
        }
    ],
    "addresses": [
        {
            "address": "123",
            "street": "Ahuizote Avenue",
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
    "member": False
}


class TestAddressViewSet(APITestCase):
    def setUp(self):
        self.user = TequioUserFactory(username='Anselmo')
        self.user.set_password('secret')
        self.user.save()
        self.client.login(username='Anselmo', password='secret')

    def test_create_contact(self):
        """
        posting valid data via the contact-list view should create a new contact
        """
        count = Contact.objects.count()
        response = self.client.post(
            reverse('contact-list'), data=NEW_CONTACT_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), count + 1)
        self.assertEqual(Contact.objects.get().last_updated_by, self.user)
        self.assertEqual(Contact.objects.get().name, 'Ricardo Flores Magon')
        # eee
