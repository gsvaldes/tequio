"""
Serializers for Contact and related models
"""
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from contacts.models import Contact, Address, Phone, Email, Tag
from users.models import TequioUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """user serializer needed for ContactSerializer"""
    class Meta:
        model = TequioUser
        fields = ('url', 'username')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """
    id added to extra_kwargs to allow updates and deletes via
    ContactSerializer
    """
    class Meta:
        model = Address
        fields = ('address', 'street', 'city', 'state',
                  'zip_code', 'country', 'url', 'id')
        extra_kwargs = {"id": {"required": False, "read_only": False}}


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    """
    id added to extra_kwargs to allow updates and deletes via
    ContactSerializer
    """
    class Meta:
        model = Phone
        fields = ('number', 'url', 'id')
        extra_kwargs = {"id": {"required": False, "read_only": False}}


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    """
    id added to extra_kwargs to allow updates and deletes via
    ContactSerializer
    """
    class Meta:
        model = Email
        fields = ('email', 'url', 'id')
        extra_kwargs = {"id": {"required": False, "read_only": False}}


class TagSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Tag
        fields = ('name', 'url', 'id')
        extra_kwargs = {"id": {"required": False, "read_only": False}}


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    """
    The Contact Serializer also updates the related
    addresses, phones, and emails and updates the last_updated_by
    field with the current logged user
    """
    created_by = UserSerializer(read_only=True)
    last_updated_by = UserSerializer(read_only=True)
    emails = EmailSerializer(many=True, required=False)
    addresses = AddressSerializer(many=True, required=False)
    phones = PhoneSerializer(many=True, required=False)
    # tags = TagSerializer(many=True, required=False)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Contact
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses', None)
        emails_data = validated_data.pop('emails', None)
        phones_data = validated_data.pop('phones', None)
        tags_data = validated_data.pop('tags', None)
        user = self.context['request'].user
        contact = Contact.objects.create(
            created_by=user,
            last_updated_by=user,
            **validated_data
        )
        if addresses_data:
            for address_data in addresses_data:
                address = Address.objects.create(**address_data)
                contact.addresses.add(address)
        if emails_data:
            for email_data in emails_data:
                email = Email.objects.create(**email_data)
                contact.emails.add(email)
        if phones_data:
            for phone_data in phones_data:
                phone = Phone.objects.create(**phone_data)
                contact.phones.add(phone)
        if tags_data:
            for tag in tags_data:
                contact.tags.add(tag)

        return contact

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('addresses', None)
        if addresses_data is not None:
            instance_addresses_mapping = {
                address.id: address for address in instance.addresses.all()}
            data_addresses_mapping = {address_data.get(
                'id'): address_data for address_data in addresses_data}

        emails_data = validated_data.pop('emails', None)
        if emails_data is not None:
            instance_emails_mapping = {
                email.id: email for email in instance.emails.all()}
            data_emails_mapping = {email_data.get(
                'id'): email_data for email_data in emails_data}

        phones_data = validated_data.pop('phones', None)
        if phones_data is not None:
            instance_phones_mapping = {
                phone.id: phone for phone in instance.phones.all()}
            data_phones_mapping = {phone_data.get(
                'id'): phone_data for phone_data in phones_data}

        tags_data = validated_data.pop('tags', None)
        instance_tags = instance.tags.all()

        instance.name = validated_data.get('name', instance.name)
        instance.member = validated_data.get('member', instance.member)
        instance.last_updated_by = self.context['request'].user
        instance.save()

        if addresses_data is not None:
            for address_id, address_data in data_addresses_mapping.items():
                address = instance_addresses_mapping.get(address_id, None)
                if address is None:
                    new_address = Address.objects.create(**address_data)
                    instance.addresses.add(new_address)
                else:
                    address.address = address_data.get(
                        'address', address.address)
                    address.street = address_data.get('street', address.street)
                    address.city = address_data.get('city', address.city)
                    address.state = address_data.get('state', address.state)
                    address.zip_code = address_data.get(
                        'zip_code', address.zip_code)
                    address.country = address_data.get(
                        'country', address.country)
                    address.save()

            for address_id, address in instance_addresses_mapping.items():
                if address_id not in data_addresses_mapping:
                    address.delete()

        if emails_data is not None:
            for email_id, email_data in data_emails_mapping.items():
                email = instance_emails_mapping.get(email_id, None)
                if email is None:
                    new_email = Email.objects.create(**email_data)
                    instance.emails.add(new_email)
                else:
                    email.email = email_data.get('email', email.email)
                    email.save()

            for email_id, email in instance_emails_mapping.items():
                if email_id not in data_emails_mapping:
                    email.delete()

        if phones_data is not None:
            for phone_id, phone_data in data_phones_mapping.items():
                phone = instance_phones_mapping.get(phone_id, None)
                if phone is None:
                    new_phone = Phone.objects.create(**phone_data)
                    instance.phones.add(new_phone)
                else:
                    phone.number = phone_data.get('number', phone.number)
                    phone.save()

            for phone_id, phone in instance_phones_mapping.items():
                if phone_id not in data_phones_mapping:
                    phone.delete()

        if tags_data is not None:
            instance.tags.set(tags_data)

        return instance
