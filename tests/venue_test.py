import unittest
from classes.venue import Venue
from classes.guest import Guest
from classes.room import Room


class TestVenue(unittest.TestCase):
    def setUp(self):
        rooms = {
            "fun": Room("fun", 5) ,
            "party": Room("party", 10)
        }
        self.venue = Venue(rooms, 70)
        self.guest_1 = Guest("steve", 100)

    def test_venue_has_rooms(self):
        self.assertEqual(2, len(self.venue.rooms))

    def test_venue_has_fee(self):
        self.assertEqual(70, self.venue.entry_fee)

    def test_venue_check_guest_in__decrease_guest_cash(self):
        self.venue.check_guest_in(self.guest_1, "fun")

        self.assertEqual(30, self.guest_1.cash)
        self.assertEqual(True, self.venue.rooms["fun"].is_guest_in_room(self.guest_1))