from rest_framework import serializers

from contacts.models import Contact, Address, Phone, Email
from users.models import TequioUser


class TequioException(Exception):
    pass


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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.member = validated_data.get('member', instance.member)
        instance.last_updated_by = self.context['request'].user

        instance.save()

        addresses_data = validated_data.pop('addresses')
        emails_data = validated_data.pop('emails')
        phones_data = validated_data.pop('phones')

        for address_data in addresses_data:
            url = address_data.get('url')
            if url:
                try:
                    address = Address.objects.get(url=url)
                except Address.DoesNotExist:
                    raise TequioException('address url: {0} does not exist'.format(url))
                address.address = address_data.get('address', address.address)
                address.street = address_data.get('street', address.street)
                address.city = address_data.get('city', address.city)
                address.state = address_data.get('state', address.state)
                address.zip_code = address_data.get('zip_code', address.zip_code)
                address.country = address_data.get('country', address.country)
                address.save()
            else:
                address = Address.objects.create(**address_data)
                instance.addresses.add(address)
                
        for email_data in emails_data:
            url = email_data.get('url')
            if url:
                try:
                    email = Email.objects.get(url=url)
                except Email.DoesNotExist:
                    raise TequioException('email url: {0} does not exist'.format(url))
                email.email = email_data.get('email', email.email)
                email.save()
            else:
                email = Email.objects.create(**email_data)
                instance.emails.add(email)

        for phone_data in phones_data:
            url = phone_data.get('url')
            if url:
                try:
                    phone = Phone.objects.get(url=url)
                except Phone.DoesNotExist:
                    raise TequioException('phone url: {0} does not exist'.format(url))
                phone.number = phone_data.get('number', phone.number)
                phone.save()
            else:
                phone = Phone.objects.create(**phone_data)
                instance.phones.add(phone)


        return instance







