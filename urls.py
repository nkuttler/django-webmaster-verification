from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^google833377565a0bbef2.html$',
        TemplateView.as_view(template_name = 'google833377565a0bbef2.html'),
        name = 'google_verify'
    ),
)
