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


Front End
+++++++++

This project uses Vue.js as the principal frontend library.
https://vuejs.org/

Webpack, https://webpack.js.org/,  is used is to bundle and compile
the JavaScript files into a single js file per page that will run 
in the browser.

Structure
---------

 - ``package.json`` has two scripts, ``dev`` and ``build``.  ``npm run build`` 
   will create a compiled file in the ``src/bundles`` directory with the name
   main-[hash].js.  ``npm run dev`` will create a similar file, but in memory
   only to be used during development.

 - ``webpack.config.js``
   - ``entry`` the entry point is for the js files to be compiled
   - ``output`` where webpack should save the compiled file and what to name it
   - ``BundleTracker`` a plugin that updates ``webpack-stats.json`` with
   the lastest bundle name

 - ``.babelrc`` The config for https://babeljs.io/

 -  ``src`` The directory for the JavaScript code.  Within this ``main.js``
     is the entry point into the vue files for a given app

Connecting to Django
--------------------

Django Webpack Loader https://github.com/ezhome/django-webpack-loader
is added to installed apps.

.. code:: python

   STATICFILES_DIRS = (
       str(ROOT_DIR('src')),
   )

   WEBPACK_LOADER = {
       'DEFAULT': {
           'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
           'STATS_FILE': str(ROOT_DIR('webpack-stats.json')),
       }
   }

In ``STATICFILES_DIRS``, we add the location of the built bundles to where
Django will look for static files. Also add the WEBPACK_LOADER setting.

To add a given bundle to a Django template use

.. code:: python

   {% load render_bundle from webpack_loader %}
   ...
   <div id="app"></div>``
   ...
   {% render_bundle 'main' %}

Where ``<div id="app"></div>`` is the element of the template that Vue will control   
and ``{% render_bundle 'main' %}`` adds the compiled script.

To pass any initial data from Django to Vue the following pattern is used

.. code:: html

   <script>
      var initial_data = {};
      initial_data.contact_list_url = '{% url "contact-list" %}';
      window.initial_data = initial_data;
   </script>

Add any initial data to a initial_data object and then add that object
to the window element.  Then within the ``main.js`` entry file. Add 

.. code:: javascript

   Vue.prototype.vue_data = window.initial_data;

initial_data will now be accessible within the vue instance
as ``this.initial_data``

Development Server
------------------

The ``server.js`` file is a local development only 
file that runs webpack-dev-server and serves the static
content on the 3000 port.

For local development, in one terminal run
``node server.js``

and in another 
``./manage.py runserver --settings.tequio.local``
or ``fab runlocal``

The current setup will still require a page refresh to 
see any static file changes.

TODO add hot reloading




   






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


Django Rest Framework
---------------------

http://www.django-rest-framework.org/
Purpose: Provide internal use only APIs

Whitenoise
----------

http://whitenoise.evans.io/
Purpose: Serve static files 
Used in place on NGINX

DJ-Database-URL
---------------

https://github.com/kennethreitz/dj-database-url
Purpose: Use Database URLs in the Django Application

django-environ
--------------

https://django-environ.readthedocs.io
Purpose: Make it easier to pull settings from ENV variables

Fabric 3
--------

Python 3 compatible fork of the original Fabric
http://docs.fabfile.org/





