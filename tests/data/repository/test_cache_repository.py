import unittest
from data.repository.cache_repository import CacheRepository


class CacheRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.cache = CacheRepository()

    def test_that_returns_Active(self):
        self.assertEqual(self.cache.get("0001", 0), 'Inactive')

    def test_that_returns_Inactive(self):
        self.assertEqual(self.cache.get("0001", 1), 'Active')
