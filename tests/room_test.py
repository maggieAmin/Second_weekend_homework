import unittest
from classes.room import Room
from classes.guest import Guest



class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("fun", 20)
        self.room_2 = Room("party", 1)
        self.guest_1 = Guest("steve", 100)
        self.guest_2 = Guest("tony", 1000)
        self.room_2.check_guest_in(self.guest_2)

    def test_room_has_name(self):
        self.assertEqual("fun", self.room_1.name)

    def test_check_guest_in__decrease_space(self):
        self.room_1.check_guest_in(self.guest_1)
        self.assertEqual(19, self.room_1.space)
        self.assertEqual(True, self.room_1.is_guest_in_room(self.guest_1))

    def test_check_guest_in__no_space(self):
        self.room_2.check_guest_in(self.guest_1)
        self.assertEqual(0, self.room_2.space)
        self.assertEqual(False, self.room_2.is_guest_in_room(self.guest_1))

    def test_check_guest_out__increase_space(self):
        self.room_2.check_guest_out(self.guest_2)
        self.assertEqual(1, self.room_2.space)
        self.assertEqual(False, self.room_2.is_guest_in_room(self.guest_2))

    def test_check_guest_out__no_guest_in_room(self):
        self.room_2.check_guest_out(self.guest_1)
        self.assertEqual(0, self.room_2.space)
        self.assertEqual(False, self.room_2.is_guest_in_room(self.guest_1))

