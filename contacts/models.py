from django.db import models

from users.models import TequioUser


class Address(models.Model):
    """Address"""
    address = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{address}-{street}-{city}-{state}-{zip}'.format(
            address=self.address,
            street=self.street,
            city=self.city,
            state=self.state,
            zip=self.zip_code
        )


class Phone(models.Model):
    """Phone"""
    number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.number


class Email(models.Model):
    """Email"""
    email = models.EmailField()

    def __str__(self):
        return self.email


class Contact(models.Model):
    """
    Contact
    """
    name = models.CharField(blank=True, max_length=255)

    addresses = models.ManyToManyField(Address, blank=True)
    phones = models.ManyToManyField(Phone, blank=True)
    emails = models.ManyToManyField(Email, blank=True)
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
