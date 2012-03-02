from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

class WebmasterVerificationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_google_file_access(self):
        url = '/googleffffffffffffffff.html'
        r = self.client.get(url)
        self.assertEqual(
            r.status_code,
            200,
            "Couldn't access %s, got %d" % (url, r.status_code)
        )

    def test_bing_file_access(self):
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

    def test_mj_file_access(self):
        url = '/MJ12_FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF.txt'
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
