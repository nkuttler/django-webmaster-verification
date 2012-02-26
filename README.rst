===========
README
===========

This application allows various webmaster tools to verify that a django site is managed by you.

The only supported method of verification is accessing xml file on your server. Only one verification code is supported at the moment.

- `Google Webmaster Tools <https://www.google.com/webmasters/tools/home>`_
- `Bing Webmaster Tools <https://ssl.bing.com/webmaster/Home/>`_
- `Majestic SEO <https://www.majesticseo.com>`_

Usage
-----

Get ``django-webmaster-verification`` into your python path::

    pip install django-webmaster-verification
    
Add ``webmaster_verification`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'webmaster_verification',
        ...
        )
    
Add ``wembaster_verification`` to your root urlconf (urls.py)::

    urlpatterns = patterns('',
        ...,
        url(r'', include('webmaster_verification.urls')),
        ...,        
    )

Add settings just as::

    WEBMASTER_VERIFICATION = {
        'google': '<google verification code>',
        'bing': '<bing verification code>',
        'majestic': '<majestic verification code>',
    }
