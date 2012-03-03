from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class WebmasterVerificationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_google_file_access_and_content(self):
        code = settings.WEBMASTER_VERIFICATION['google']
        url = self._get_google_url(code)
        r = self.client.get(url)
        self.assertEqual(
            r.status_code,
            200,
            "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertRegexpMatches(
            r.content,
            '.*%s.*' % code,
            'Verification code not found in response body',
        )

    def _get_google_url(self, code):
        return '/google%s.html' % code

    def test_bing_file_access_and_content(self):
        code = settings.WEBMASTER_VERIFICATION['bing']
        url = '/BingSiteAuth.xml'
        r = self.client.get(url)
        self.assertEqual(
            r.status_code,
            200,
            "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertEqual(
            r['Content-Type'],
            'text/xml',
            "Got %s content type for robots.txt" % r['Content-Type']
        )
        self.assertRegexpMatches(
            r.content,
            '.*%s.*' % code,
            'Verification code not found in response body',
        )

    def test_mj_file_access(self):
        url = self._get_mj_url(settings.WEBMASTER_VERIFICATION['majestic'])
        r = self.client.get(url)
        self.assertEqual(
            r.status_code,
            200,
            "Couldn't access %s, got %d" % (url, r.status_code)
        )
        self.assertEqual(
            r['Content-Type'],
            'text/plain',
            "Got %s content type for robots.txt" % r['Content-Type']
        )

    def _get_mj_url(self, code):
        return '/MJ12_%s.txt' % code
