from django.views.generic import TemplateView

import settings


class GoogleVerifyView(TemplateView):
    template_name = 'google_verify_template.html'

    def get_context_data(self, **kwargs):
        context = super(GoogleVerifyView, self).get_context_data(**kwargs)
        context['google_verification'] = settings.VERIFICATION['google']
        return context


class BingVerifyView(TemplateView):
    template_name = 'bing_verify_template.xml'

    def get_context_data(self, **kwargs):
        context = super(BingVerifyView, self).get_context_data(**kwargs)
        context['bing_verification'] = settings.VERIFICATION['bing']
        return context
