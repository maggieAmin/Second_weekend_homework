import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("feeling good")

    def test_song_has_name(self):
        self.assertEqual("feeling good", self.song_1.name)