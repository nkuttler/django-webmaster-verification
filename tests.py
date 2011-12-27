from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class GoogleVerifyTest(TestCase):
    def setUp(self):
        self.client = Client()
        url = reverse('google_verify')
        self.r = self.client.get(url)

    def test_google_verification_file_can_be_accessed(self):
        self.assertEqual(
            self.r.status_code,
            200,
            "Couldn't access the google verification file, got %d"
                                                        % self.r.status_code
        )

    def test_google_verification_file_has_right_content(self):
        self.assertRegexpMatches(
            self.r.content,
            'google-site-verification: google833377565a0bbef2.html',
            'fuck'
        )
