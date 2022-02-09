from django.conf import settings
from django.test import override_settings
from django.test import TestCase
from django.test.client import Client


conf_multi = {
    "bing": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "google": (
        "ffffffffffffffff",
        "aaaaaaaaaaaaaaaa",
    ),
    "majestic": (
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ),
    "yandex": (
        "f0f0f0f0f0f0f0f0",
        "1919191919191919",
    ),
    "alexa": (
        "1234567890abcdefABCDEF12345",
        "12345abcdef1234567890ABCDEF",
    ),
}

conf = {
    "bing": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "google": "ffffffffffffffff",
    "majestic": "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
    "yandex": "f0f0f0f0f0f0f0f0",
    "alexa": "12345abcdef1234567890ABCDEF",
}


class WebmasterVerificationMixin:
    def setUp(self):
        self.client = Client()


class GoogleMixin:
    def test_google_file_access_and_content(self):
        if "google" in settings.WEBMASTER_VERIFICATION:
            codes = settings.WEBMASTER_VERIFICATION["google"]
            if type(codes) == tuple:
                for code in codes:
                    self._test_google_file_access_and_content(code)
            else:
                self._test_google_file_access_and_content(codes)

    def _test_google_file_access_and_content(self, code):
        """
        Test if the google verification file for a specific code exists and if
        it's content is correct.
        """
        url = self._get_google_url(code)
        r = self.client.get(url)
        self.assertEqual(
            r.status_code, 200, "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertRegex(
            str(r.content),
            r".*google{}\.html.*".format(code),
            "Verification code not found in response body",
        )

    def test_google_file_404s(self):
        bad_codes = (
            "",
            "012345678",
            "0123456789abcdef",
        )
        for code in bad_codes:
            url = self._get_google_url(code)
            r = self.client.get(url)
            self.assertEqual(
                r.status_code,
                404,
                "Could access %s for inexistent code, got %d" % (url, r.status_code),
            )

    def _get_google_url(self, code):
        return "/google%s.html" % code


class BingMixin:
    def test_bing_file_access_and_content(self):
        if "bing" in settings.WEBMASTER_VERIFICATION:
            code = settings.WEBMASTER_VERIFICATION["bing"]
            url = "/BingSiteAuth.xml"
            r = self.client.get(url)
            self.assertEqual(
                r.status_code, 200, "Couldn't access %s, got %d" % (url, r.status_code)
            )
            self.assertEqual(
                r["Content-Type"],
                "text/xml",
                "Got %s content type for xml file" % r["Content-Type"],
            )
            self.assertRegex(
                str(r.content),
                ".*%s.*" % code,
                "Verification code not found in response body",
            )


class MajesticMixin:
    def test_mj_file_access(self):
        if "majestic" in settings.WEBMASTER_VERIFICATION:
            codes = settings.WEBMASTER_VERIFICATION["majestic"]
            if type(codes) == tuple:
                for code in codes:
                    self._test_mj_file_access(code)
            else:
                self._test_mj_file_access(codes)

    def _test_mj_file_access(self, code):
        url = self._get_mj_url(code)
        r = self.client.get(url)
        self.assertEqual(
            r.status_code, 200, "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertEqual(
            r["Content-Type"],
            "text/plain",
            "Got %s content type for text file" % r["Content-Type"],
        )

    def test_mj_file_404s(self):
        bad_codes = (
            "",
            "012345678",
            "0123456789ABCDEF0123456789ABCDEF",
        )
        for code in bad_codes:
            url = self._get_mj_url(code)
            r = self.client.get(url)
            self.assertEqual(
                r.status_code,
                404,
                "Could access %s for inexistent code, got %d" % (url, r.status_code),
            )

    def _get_mj_url(self, code):
        return "/MJ12_%s.txt" % code


class YandexMixin:
    # TODO look into refactoring this
    def _test_yandex_file_access(self, code):
        url = self._get_yandex_url(code)
        r = self.client.get(url)
        self.assertEqual(
            r.status_code, 200, "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertEqual(
            r["Content-Type"],
            "text/plain",
            "Got %s content type for text file" % r["Content-Type"],
        )

    # TODO look into refactoring this
    def _get_yandex_url(self, code):
        return "/yandex_%s.html" % code

    # TODO look into refactoring this
    def test_yandex_file_acces(self):
        if "yandex" in settings.WEBMASTER_VERIFICATION:
            codes = settings.WEBMASTER_VERIFICATION["yandex"]
            if type(codes) == tuple:
                for code in codes:
                    self._test_yandex_file_access(code)
            else:
                self._test_yandex_file_access(codes)

    # TODO look into refactoring this
    def test_yandex_file_404s(self):
        bad_codes = (
            "",
            "012345678",
            "0123456789ABCDEF0123456789ABCDEF",
        )
        for code in bad_codes:
            url = self._get_yandex_url(code)
            r = self.client.get(url)
            self.assertEqual(
                r.status_code,
                404,
                "Could access %s for inexistent code, got %d" % (url, r.status_code),
            )


class AlexaMixin:
    # TODO look into refactoring this
    def _test_alexa_file_access(self, code):
        url = self._get_alexa_url(code)
        r = self.client.get(url)
        self.assertEqual(
            r.status_code, 200, "Couldn't access %s, got %d" % (url, r.status_code)
        )

    # TODO look into refactoring this
    def _get_alexa_url(self, code):
        return "/%s.html" % code

    # TODO look into refactoring this
    def test_alexa_file_acces(self):
        if "alexa" in settings.WEBMASTER_VERIFICATION:
            codes = settings.WEBMASTER_VERIFICATION["alexa"]
            if type(codes) == tuple:
                for code in codes:
                    self._test_alexa_file_access(code)
            else:
                self._test_alexa_file_access(codes)

    # TODO look into refactoring this
    def test_alexa_file_404s(self):
        bad_codes = (
            "",
            "012345678",
            "0123456789ABCDEF0123456789ABCDEF",
        )
        for code in bad_codes:
            url = self._get_alexa_url(code)
            r = self.client.get(url)
            self.assertEqual(
                r.status_code,
                404,
                "Could access %s for inexistent code, got %d" % (url, r.status_code),
            )


@override_settings(WEBMASTER_VERIFICATION=conf)
class AlexaTest(WebmasterVerificationMixin, AlexaMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf)
class BingTest(WebmasterVerificationMixin, BingMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf)
class GoogleTest(WebmasterVerificationMixin, GoogleMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf)
class MajesticTest(WebmasterVerificationMixin, MajesticMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf)
class YandexTest(WebmasterVerificationMixin, YandexMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf_multi)
class AlexaMultiTest(WebmasterVerificationMixin, AlexaMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf_multi)
class BingMultiTest(WebmasterVerificationMixin, BingMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf_multi)
class GoogleMultiTest(WebmasterVerificationMixin, GoogleMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf_multi)
class MajesticMultiTest(WebmasterVerificationMixin, MajesticMixin, TestCase):
    pass


@override_settings(WEBMASTER_VERIFICATION=conf_multi)
class YandexMultiTest(WebmasterVerificationMixin, YandexMixin, TestCase):
    pass
