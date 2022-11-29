import unittest
from unittest import mock

from data.repository.cache_repository import CacheRepository
from data.repository.discount_repository import DiscountRepository


class DiscountRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.repository = DiscountRepository()

    def mocked_success_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, text, status_code):
                self.text = text
                self.status_code = status_code

            def json(self):
                return self.text

        return MockResponse('[30]', 200)

    def mocked_error_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.status_code = status_code

        return MockResponse(None, 404)

    @mock.patch('requests.get', side_effect=mocked_error_requests_get)
    def test_that_returns_default_discount_when_error(self, mock_get):
        self.assertEqual(self.repository.get_discount(), 10)

    @mock.patch('requests.get', side_effect=mocked_success_requests_get)
    def test_that_returns_random_discount(self, mock_get):
        self.assertEqual(self.repository.get_discount(), 30)
