from django.conf.urls.defaults import patterns, include, url

from views import GoogleVerificationView
from views import BingVerificationView

urlpatterns = patterns('',
    url(
        r'^google[0-9a-f]{16}.html$',
        GoogleVerificationView.as_view(),
        name = 'google_verify'
    ),
    url(
        r'^BingSiteAuth.xml$',
        BingVerificationView.as_view(),
        name = 'bing_verify'
    ),
)
