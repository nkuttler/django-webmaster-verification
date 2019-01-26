from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('webmaster_verification.urls')),
]
