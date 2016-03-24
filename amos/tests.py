# django
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client

# own modules
from .factories import UserFactory
from .utils import url_with_querystring

from django.contrib.auth.models import User


class HomePageTest(TestCase):

    """
    Tests for home page
    """

    def setUp(self):
        self.user = UserFactory(username='test_user')
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_page_denies_anonymous(self):
        target_url = reverse('amos_index')
        redirect_url = url_with_querystring(reverse('login'), 'next=/amos/')
        response = self.client.get(target_url, follow=True)
        self.assertRedirects(response, redirect_url)
        response = self.client.post(target_url, follow=True)
        self.assertRedirects(response, redirect_url)

    def test_home_page_accepts_user(self):
        self.client.force_login(self.user)
        target_url = reverse('amos_index')
        response = self.client.get(target_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
