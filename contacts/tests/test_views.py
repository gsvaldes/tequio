from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from test_utils.user_factories import TequioUserFactory
from contacts.models import Contact, Address, Email, Phone


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

NEW_CONTACT_DATA2 = {
    "emails": [
        {
            "email": "tierra@libertad.org"
        }
    ],
    "addresses": [
        {
            "address": "456",
            "street": "Ahuizote Avenue",
            "city": "New Haven",
            "state": "CT",
            "zip_code": "06511",
            "country": "USA",
        }
    ],
    "phones": [
        {
            "number": "7775551234",
        }
    ],
    "name": "Enrique Flores Magon",
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

    def test_update_existing_contact(self):
        """
        Update the Contact fields and related email, address, and phone
        fields
        """
        contact = Contact.objects.create(name='Enrique Flores Magon')
        email = Email.objects.create(email='original@regeneracion.org')
        contact.emails.add(email)
        address = Address.objects.create(city='Original City')
        contact.addresses.add(address)
        phone = Phone.objects.create(number='1111111111')
        contact.phones.add(phone)

        data = {
            "emails": [
                {
                    "email": "changed@regeneracion.org",
                    "id": email.id
                }
            ],
            "addresses": [
                {
                    "city": "New City",
                    "id": address.id
                }
            ],
            "phones": [
                {
                    "number": "2222222222",
                    "id": phone.id
                }
            ],
            "name": "Enrique Flores Magon",
            "member": True
        }

        response = self.client.put(
            reverse('contact-detail', kwargs={'pk': contact.id}),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_contact = Contact.objects.get(name='Enrique Flores Magon')

        self.assertTrue(
            'changed@regeneracion.org' in
            [email.email for email
             in updated_contact.emails.all()],
        )
        self.assertFalse(
            'original@regeneracion.org' in
            [email.email for email
             in updated_contact.emails.all()],
        )
        self.assertTrue(
            '2222222222' in
            [phone.number for phone
             in updated_contact.phones.all()],
        )
        self.assertFalse(
            '1111111111' in
            [phone.number for phone
             in updated_contact.phones.all()],
        )
        self.assertTrue(
            'New City' in
            [address.city for address
             in updated_contact.addresses.all()],
        )
        self.assertFalse(
            'Original City' in
            [address.city for address
             in updated_contact.addresses.all()],
        )

    def test_omitted_field_in_update_is_not_altered(self):
        """
        Omitting the many to many fields in an update to
        the ContactSerializer, phones, addresses, or emails
        should not alter the existing data or create new related
        entries.
        """
        contact = Contact.objects.create(name='Genovevo de la O')
        email = Email.objects.create(email='original@example.org')
        contact.emails.add(email)
        address = Address.objects.create(zip_code='12345')
        contact.addresses.add(address)
        phone = Phone.objects.create(number='5551212')
        contact.phones.add(phone)

        data = {
            "name": 'Genovevo de la O',
            "member": True
        }

        response = self.client.put(
            reverse('contact-detail', kwargs={'pk': contact.id}),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_contact = Contact.objects.get(name='Genovevo de la O')
        self.assertEqual(updated_contact.emails.count(), 1)
        self.assertEqual(updated_contact.phones.count(), 1)
        self.assertEqual(updated_contact.addresses.count(), 1)
        self.assertEqual(
            updated_contact.emails.first().email,
            'original@example.org'
        )
        self.assertEqual(updated_contact.phones.first().number, '5551212')
        self.assertEqual(updated_contact.addresses.first().zip_code, '12345')

    def test_empty_list_as_value_deletes_related_fields(self):
        """
        Passing an empty list as the value for phones, addresses, or emails
        should delete any existing related entries.
        """
        contact = Contact.objects.create(name='Palomares')
        email = Email.objects.create(email='original@example.org')
        contact.emails.add(email)
        address = Address.objects.create(zip_code='12345')
        contact.addresses.add(address)
        phone = Phone.objects.create(number='5551212')
        contact.phones.add(phone)

        data = {
            "member": True,
            "name": "Palomares",
            "addresses": [],
            "emails": [],
            "phones": []
        }

        response = self.client.put(
            reverse('contact-detail', kwargs={'pk': contact.id}),
            data=data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_contact = Contact.objects.get(name='Palomares')
        self.assertEqual(updated_contact.emails.count(), 0)
        self.assertEqual(updated_contact.phones.count(), 0)
        self.assertEqual(updated_contact.addresses.count(), 0)
