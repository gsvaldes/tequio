from django.contrib import admin

from contacts.models import Contact, Address, Phone, Email

admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)
