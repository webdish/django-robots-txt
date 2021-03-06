======
README
======

This is a simple application to create a ``robots.txt`` file for django. It has no models at all and you're supposed to edit a template to update the ``robots.txt`` file. I got tired of having to add this view to each and every project because Django doesn't have a built in ``text/plain`` view.

See the `robots page <http://www.robotstxt.org/>`_ for details what the file should look like.

.. image:: https://api.travis-ci.org/nkuttler/django-robots-txt.png
  :target: https://travis-ci.org/nkuttler/django-robots-txt

Usage
-----

Get ``django-robots-txt`` into your python path::

    pip install django-robots-txt

Create your custom robots.txt file in one of your template directories as ``robots_txt/robots.txt``.

Add a ``robots.txt`` view to your root ``urls.py``::

    from django.conf.urls.defaults import patterns, include, url
    from robots_txt.views import RobotsTextView

    urlpatterns = patterns('',
        ...,
        url(r'^robots.txt$', RobotsTextView.as_view()),
        ...,
    )

That's it, your robots.txt template will be served.

This urlconf entry is also supported if you prefer to keep it short::

    urlpatterns = patterns('',
        ...,
        url(r'', include('robots_txt.urls')),
        ...,
    )

You can add ``robots_txt`` to your INSTALLED_APPS in settings.py if you don't want to create your own template and don't mind having an empty ``robots.txt``::

    INSTALLED_APPS = (
        ...,
        'robots_txt',
        ...,
    )

Changes
-------
0.4:
- Refactor tests
- Updates for Django 1.6

0.3:
- Bugfix for included urlconfig
