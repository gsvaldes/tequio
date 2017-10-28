from django.db import models

from users.models import TequioUser

# Create your models here.

class Address(models.Model):
    """
    """
    address = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=100, blank=True)


class Phone(models.Model):
    number = models.CharField(max_length=50, blank=True)


class Email(models.Model):
    email = models.EmailField()


class Contact(models.Model):
    """
    """
    name = models.CharField(blank=True, max_length=255)

    addresses = models.ManyToManyField(Address, blank=True)
    phones = models.ManyToManyField(Phone, blank=True)
    emails = models.ManyToManyField(Email, blank=True)

    created_by = models.ForeignKey(TequioUser, related_name="contact_created_by", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    last_updated_by = models.ForeignKey(TequioUser, related_name="contact_updated_by", on_delete=models.CASCADE)
    last_updated_on = models.DateTimeField(auto_now=True)

    #  TODO custom save to add user to created_by and last_updated_by
