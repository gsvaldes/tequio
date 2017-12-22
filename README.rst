======
tequio
======

*Membership engagement for mutual aid*

Overview
++++++++

Local Development
+++++++++++++++++

The project uses the multiple settings.py structure recommended in Two 
scoops of Django.  Because of this, the setting file to use must be 
specified.

To run locally
``./manage.py runserver --settings=tequio.settings.local``

The fabric shortcut is
``fab runlocal``

Similarly, to use the shell
``./manage.py shell --settings=tequio.settings.local``
or 
``fab shelllocal``


Users
+++++

The ``TequioUser model`` subclasses Django's ``AbstractUser`` model, but does not yet add
any additional fields or functionality.

Contacts, Members, Volunteers, etc. are not tied to the User model.  It's
expected that organization members who have access to the site, and hence have TequioUser record,
are a limited subset of an organization's members and volunteers.

User Creation
-------------

User creation is based in part on 
http://django-authtools.readthedocs.io/en/latest/how-to/invitation-email.html
and also https://medium.com/@khansubhan95/password-reset-in-django-8b4d37924958
although, Tequio does not use django-authools itself.

When a new TequioUser is created via the admin page, an initial random, 
unknowable password is created and the new user is sent a password
reset email. 



Testing
+++++++

Deployment
++++++++++

Heroku Specific
---------------

``Procfile``
``runtime.txt``


Third Party Tools Used
++++++++++++++++++++++

Whitenoise
----------

http://whitenoise.evans.io/
Purpose: Serve static files 
Used in place on NGINX

django-environ
--------------

https://django-environ.readthedocs.io
Purpose: Make it easier to pull settings from ENV variables





