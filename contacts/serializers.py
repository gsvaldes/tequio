from rest_framework import serializers

from contacts.models import Contact, Address, Phone, Email
from users.models import TequioUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TequioUser
        fields = ('url', 'username')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer(read_only=True)
    last_updated_by = UserSerializer(read_only=True)
    emails = EmailSerializer(many=True)
    addresses = AddressSerializer(many=True)
    phones = PhoneSerializer(many=True)


    class Meta:
        model = Contact
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        addresses_data = validated_data.pop('addresses')
        emails_data = validated_data.pop('emails')
        phones_data = validated_data.pop('phones')
        user = self.context['request'].user
        contact = Contact.objects.create(
            created_by=user,
            last_updated_by=user,
            **validated_data
        )
        for address_data in addresses_data:
            address = Address.objects.create(**address_data)
            contact.addresses.add(address)

        for email_data in emails_data:
            email = Email.objects.create(**email_data)
            contact.emails.add(email)

        for phone_data in phones_data:
            phone = Phone.objects.create(**phone_data)
            contact.phones.add(phone)
        
        return contact







