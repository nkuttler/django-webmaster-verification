from django.urls import re_path

from webmaster_verification.views import AlexaVerificationView
from webmaster_verification.views import BingVerificationView
from webmaster_verification.views import GoogleVerificationView
from webmaster_verification.views import MajesticVerificationView
from webmaster_verification.views import YandexVerificationView


urlpatterns = [
    re_path(
        r"^google(?P<code>[0-9a-f]{16})\.html$",
        GoogleVerificationView.as_view(),
        name="google_verify",
    ),
    re_path(r"^BingSiteAuth\.xml$", BingVerificationView.as_view(), name="bing_verify"),
    re_path(
        r"^MJ12_(?P<code>[0-9A-F]{32})\.txt$",
        MajesticVerificationView.as_view(),
        name="majestic_verify",
    ),
    re_path(
        r"^yandex_(?P<code>[0-9a-f]{16})\.html$",
        YandexVerificationView.as_view(),
        name="majestic_verify",
    ),
    re_path(
        r"^(?P<code>[0-9a-zA-Z]{27})\.html$",
        AlexaVerificationView.as_view(),
        name="alexa_verify",
    ),
]
