import uuid
from django.db import models

from users.models import TequioUser


class Address(models.Model):
    """Address"""
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{address}-{city}-{state}-{zip}'.format(
            address=self.address,
            city=self.city,
            state=self.state,
            zip=self.zip_code
        )


class Phone(models.Model):
    """Phone"""
    number = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{number}-{type}'.format(
            number=self.number,
            type=self.type
        )


class Email(models.Model):
    """Email"""
    email = models.EmailField()

    def __str__(self):
        return self.email


class Tag(models.Model):
    """
    Tag for contacts.  
    see 
    http://tinystruggles.com/2015/06/04/django-api-resource-with-tags.html
    """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return 'Tag[id: {id}, name: {name}]'.format(
            id=self.id, name=self.name
        )


class Contact(models.Model):
    """
    Contact
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # TODO null has no effect on many to many field
    addresses = models.ManyToManyField(Address, blank=True)
    phones = models.ManyToManyField(Phone, blank=True)
    emails = models.ManyToManyField(Email, blank=True)
    tags = models.ManyToManyField(Tag, related_name='contacts')
    created_by = models.ForeignKey(
        TequioUser,
        related_name="contact_created_by",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(
        TequioUser,
        related_name="contact_updated_by",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    last_updated_on = models.DateTimeField(auto_now=True)

    member = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    """
    Comments
    """
    contact = models.ForeignKey(
        'Contact', related_name='notes', on_delete=models.CASCADE)
    note = models.TextField()
    created_by = models.ForeignKey(
        TequioUser,
        related_name="note_created_by",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(
        TequioUser,
        related_name="note_updated_by",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        # TODO add formatted last_updated_on to str
        return self.contact


