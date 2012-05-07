======
README
======

This application allows various webmaster tools to verify that a django site is managed by you.

The only supported method of verification is by accessing a file on your server. Only one verification code per service provider is supported at the moment.

Supported services:

- `Google Webmaster Tools <https://www.google.com/webmasters/tools/home>`_
- `Bing Webmaster Tools <https://ssl.bing.com/webmaster/Home/>`_
- `Majestic SEO <https://www.majesticseo.com>`_

Usage
-----

Get ``django-webmaster-verification`` into your python path::

    pip install django-webmaster-verification

Add ``webmaster_verification`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...,
        'webmaster_verification',
        ...,
    )

Add ``wembaster_verification`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r'', include('webmaster_verification.urls')),
        ...,
    )

Add settings just as::

    WEBMASTER_VERIFICATION = {
        'bing': '<bing verification code>',
        'google': '<google verification code>',
        'majestic': '<majestic verification code>',
    }

Multiple codes for google an majestic are supported as well::

    WEBMASTER_VERIFICATION = {
        'bing': '<bing verification code>',
        'google': (
                '<google verification code 1>',
                '<google verification code 2>',
        ),
        'majestic': (
                '<majestic verification code 1>',
                '<majestic verification code 2>',
        ),
    }

As bing always accesses the same verification file I'm not sure if it's possible to support more than one code for it.

Changelog
=========

0.1.7 (2012-05-07)
------------------

Bugfix for multiple verification codes for one provider.
