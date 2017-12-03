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


Testing
+++++++

Deployment
++++++++++

