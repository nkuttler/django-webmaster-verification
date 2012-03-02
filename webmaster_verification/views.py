import logging
logger = logging.getLogger(__name__)

from django.http import Http404
from django.views.generic import TemplateView

from django.conf import settings


class VerificationView(TemplateView):
    """
    This simply adds the verification key to the view context and makes sure
    we return a 404 if the key wasn't set for the provider
    """
    def get_context_data(self, **kwargs):
        context = super(VerificationView, self).get_context_data(**kwargs)
        try:
            context['%s_verification' % self.provider] = settings.WEBMASTER_VERIFICATION[self.provider]
        except KeyError:
            raise Http404
        except AttributeError:
            logger.info("WEBMASTER_VERIFICATION not defined in settings")
            raise Http404
        return context


class VerificationTextView(VerificationView):
    """
    Return proper content type
    """
    def render_to_response(self, context, **kwargs):
        return super(VerificationTextView, self).render_to_response(
            context,
            content_type='text/plain',
            **kwargs
        )


class VerificationXMLView(VerificationView):
    """
    Return proper content type
    """
    def render_to_response(self, context, **kwargs):
        return super(VerificationXMLView, self).render_to_response(
            context,
            content_type='text/xml',
            **kwargs
        )

class GoogleVerificationView(VerificationView):
    template_name = 'webmaster_verification/google_verify_template.html'
    provider = 'google'


class BingVerificationView(VerificationXMLView):
    template_name = 'webmaster_verification/bing_verify_template.xml'
    provider = 'bing'


class MajesticVerificationView(VerificationTextView):
    template_name = 'webmaster_verification/majestic_verify_template.txt'
    provider = 'majestic'
