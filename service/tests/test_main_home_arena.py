from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class MainHomeArenaTest(TestCase):
    def test_main_home_arena_view(self):
        client = Client()
        self.assertEqual(True, True)
