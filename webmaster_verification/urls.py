from django.conf.urls.defaults import patterns, include, url

from views import GoogleVerificationView
from views import BingVerificationView
from views import MajesticVerificationView

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
    url(
        r'^MJ12_[0-9A-F]{32}.txt$',
        MajesticVerificationView.as_view(),
        name = 'majestic_verify'
    ),
)
