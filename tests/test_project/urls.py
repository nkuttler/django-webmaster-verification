from django.conf.urls.defaults import patterns, include, url

from django.views.generic import TemplateView
from webmaster_verification.views import BingVerificationView

urlpatterns = patterns('',
    url(r'^x$', TemplateView.as_view(template_name = 'x')),
    url(r'', include('webmaster_verification.urls')),
)
