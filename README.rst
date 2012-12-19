======
README
======

This application allows various webmaster tools to verify that a django site is managed by you.

The only supported method of verification is by accessing a file on your server.

Supported services:

- `Google Webmaster Tools <https://www.google.com/webmasters/tools/home>`_
- `Bing Webmaster Tools <https://ssl.bing.com/webmaster/Home/>`_
- `Yandex Webmaster Tools <http://webmaster.yandex.com/>`_
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
        'yandex': '<yandex verification code>',
    }

The codes are alphanumeric and don't include suffixes like 'html', e.g.
``847e1f379a99c28a`` for google, not ``847e1f379a99c28a.html``.

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
        'yandex': (
                '<yandex verification code 1>',
                '<yandex verification code 2>',
        ),
    }

As bing always accesses the same verification file I'm not sure if it's possible to support more than one code for it. Please let me know if yes and how, as I don't really use their tools.

For Yandex only the .txt file method is supported, but adding support for .html
should be trivial.

Changelog
=========

0.1.9 (2012-12-19)
------------------

- Pypi updates

0.1.8 (2012-12-19)
------------------

- Yandex Webmaster Tools support added.

0.1.7 (2012-05-07)
------------------

- Bugfix for multiple verification codes for one provider.
