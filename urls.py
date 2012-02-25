from django.conf.urls.defaults import patterns, include, url

from views import GoogleVerifyView
from views import BingVerifyView

urlpatterns = patterns('',
    url(
        r'^google[0-9a-f]{16}.html$',
        GoogleVerifyView.as_view(),
        name = 'google_verify'
    ),
    url(
        r'^BingSiteAuth.xml$',
        BingVerifyView.as_view(),
        name = 'bing_verify'
    ),
)
