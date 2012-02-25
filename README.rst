===========
README
===========

This django application allows various webmaster tools to quickly verify that the site is managed by you.

Currently Google and Bing webmaster tools are supported.

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
    }
