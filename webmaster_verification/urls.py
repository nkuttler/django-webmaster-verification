from django.conf.urls import url

from .views import AlexaVerificationView
from .views import BingVerificationView
from .views import GoogleVerificationView
from .views import MajesticVerificationView
from .views import YandexVerificationView


urlpatterns = [
    url(
        r"^google(?P<code>[0-9a-f]{16})\.html$",
        GoogleVerificationView.as_view(),
        name="google_verify",
    ),
    url(r"^BingSiteAuth\.xml$", BingVerificationView.as_view(), name="bing_verify"),
    url(
        r"^MJ12_(?P<code>[0-9A-F]{32})\.txt$",
        MajesticVerificationView.as_view(),
        name="majestic_verify",
    ),
    url(
        r"^yandex_(?P<code>[0-9a-f]{16})\.html$",
        YandexVerificationView.as_view(),
        name="majestic_verify",
    ),
    url(
        r"^(?P<code>[0-9a-zA-Z]{27})\.html$",
        AlexaVerificationView.as_view(),
        name="alexa_verify",
    ),
]
