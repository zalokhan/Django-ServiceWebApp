from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class MainHomeArenaTest(TestCase):
    def test_main_home_arena_view(self):
        client = Client()
        response = client.get(reverse('service:main_home'))
        self.assertEqual(response.status_code, 200)
