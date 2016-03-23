# django
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

# own modules
from .factories import UserFactory
from .utils import url_with_querystring


class HomePageTest(TestCase):

    """
    Tests for home page
    """

    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.client = Client()

    def test_call_view_denies_anonymous(self):
        target_url = reverse('amos_index')
        redirect_url = url_with_querystring(reverse('login'), 'next=/amos/')
        response = self.client.get(target_url, follow=True)
        self.assertRedirects(response, redirect_url)
        response = self.client.post(target_url, follow=True)
        self.assertRedirects(response, redirect_url)
