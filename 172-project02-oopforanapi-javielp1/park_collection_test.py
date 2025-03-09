import json
import unittest

from park_collection import ParkCollection


class TestParkCollection(unittest.TestCase):

    def test_get_parks_by_state(self):
        with open('park_json.json', 'r', encoding='utf-8') as park_json_file:
            park_json = json.load(park_json_file)
            parks_in_maine = ParkCollection('park_json', park_json)
            self.assertEqual(parks_in_maine.get_parks_by_state('ME'), 44)
            parks_in_NY = ParkCollection('park_json', park_json)
            self.assertEqual(parks_in_NY.get_parks_by_state('NY'), 173)


    def test_find_parks_by_activities(self):
        with open('park_json.json', 'r', encoding='utf-8') as parks_json_file:
            park_json = json.load(parks_json_file)
            parks_with_arts_and_culture = ParkCollection('park_json', park_json)
            self.assertEqual(parks_with_arts_and_culture.get_parks_with_activities('Arts and Culture'),157)


