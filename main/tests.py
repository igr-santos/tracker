from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ProjectTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user_data = {
            'username': 'root',
            'password': '1234'
        }
        User.objects.create_superuser(
            email='root@localhost.com',
            **self.user_data
        )

    def _get_path(self, resp):
        return resp.url.replace('http://testserver', '')

    def test_login_system(self):
        resp = self.c.post(reverse('login'), self.user_data)
        self.assertEqual(resp.status_code, 302)

        expected_redirect = reverse('main:index')
        self.assertEqual(self._get_path(resp), expected_redirect)
