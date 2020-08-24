import logging

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class FileAccessMixin(object):
    """
    Make sure the code for the accessed file is configured.

    We don't want to add billions of files to sites. This is necessary
    for foo-<code> like filenames.
    """

    def get(self, request, *args, **kwargs):
        try:
            if (
                self.kwargs["code"] not in settings.WEBMASTER_VERIFICATION[self.provider]
                and self.kwargs["code"] != settings.WEBMASTER_VERIFICATION[self.provider]
            ):
                raise Http404
        except KeyError:
            raise Http404
        return super(FileAccessMixin, self).get(request, *args, **kwargs)


class MimeTextMixin(object):
    """
    Return text content type.
    """

    def render_to_response(self, context, **kwargs):
        return super(MimeTextMixin, self).render_to_response(
            context, content_type="text/plain", **kwargs
        )


class MimeXMLMixin(object):
    """
    Return xml content type.
    """

    def render_to_response(self, context, **kwargs):
        return super(MimeXMLMixin, self).render_to_response(
            context, content_type="text/xml", **kwargs
        )


class VerificationView(TemplateView):
    """
    This adds the verification key to the template context and makes sure we
    return a 404 if no key was set for the provider.
    """

    def get_context_data(self, **kwargs):
        context = super(VerificationView, self).get_context_data(**kwargs)
        try:
            codes = settings.WEBMASTER_VERIFICATION[self.provider]
            if "code" in self.kwargs:
                if self.kwargs["code"] in codes or self.kwargs["code"] == codes:
                    code = self.kwargs["code"]
            else:
                code = codes
            context["%s_verification" % self.provider] = code
        except KeyError:
            raise Http404
        except AttributeError:
            logger.info("WEBMASTER_VERIFICATION not defined in settings")
            raise Http404
        return context


class GoogleVerificationView(FileAccessMixin, VerificationView):
    template_name = "webmaster_verification/google_verify_template.html"
    provider = "google"


class BingVerificationView(MimeXMLMixin, VerificationView):
    template_name = "webmaster_verification/bing_verify_template.xml"
    provider = "bing"


class MajesticVerificationView(MimeTextMixin, FileAccessMixin, VerificationView):
    template_name = "webmaster_verification/majestic_verify_template.txt"
    provider = "majestic"


class YandexVerificationView(MimeTextMixin, FileAccessMixin, VerificationView):
    template_name = "webmaster_verification/yandex_verify_template.html"
    provider = "yandex"


class AlexaVerificationView(FileAccessMixin, VerificationView):
    template_name = "webmaster_verification/alexa_verify_template.html"
    provider = "alexa"
