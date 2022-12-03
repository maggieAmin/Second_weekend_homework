import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("steve", 100)

    def test_guest_has_name(self):
        self.assertEqual("steve", self.guest_1.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest_1.cash)

    def test_guest_can_afford__has_money(self):
        afford = self.guest_1.can_afford(30)
        self.assertEqual(True, afford)

    def test_guest_can_afford__has_no_money(self):
        afford = self.guest_1.can_afford(200)
        self.assertEqual(False, afford)

    def test_remove_money(self):
        self.guest_1.remove_money(30)
        self.assertEqual(70, self.guest_1.cash)