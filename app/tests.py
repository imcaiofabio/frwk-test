from django.test import TestCase
import requests
from app.views import MAIN_ENDPOINT

RESPONSE_MAIN_ENDPOINT = requests.get(MAIN_ENDPOINT)


class UsersTests(TestCase):
    def test_endpoint_status_code(self):
        self.assertEqual(RESPONSE_MAIN_ENDPOINT.status_code, 200)

    def test_endpoint_json_keys(self):
        expect_keys = ['userId', 'id', 'title', 'completed']
        self.assertEqual(list(RESPONSE_MAIN_ENDPOINT.json()[0].keys()), expect_keys)

    def test_endpoint_has_more_than_five_items(self):
        total_items = len(RESPONSE_MAIN_ENDPOINT.json())
        self.assertGreaterEqual(total_items, 5)
