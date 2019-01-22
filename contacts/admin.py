from django.contrib import admin

from contacts.models import Contact, Address, Phone, Email, Tag, Note

admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Tag)
admin.site.register(Note)
