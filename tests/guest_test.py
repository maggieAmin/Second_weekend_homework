import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("steve", 100)
    def test_guest_has_name(self):
        self.assertEqual("steve", self.guest_1.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest_1.cash)
