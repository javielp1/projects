import unittest
from park_collection import ParkCollection
import json


class TestParkCollection(unittest.TestCase):
    def test_get_parks_list(self):
        with open('park_json.json') as file:
            park_json = json.load(file)
            park_collection = ParkCollection(park_json)
            self.assertEqual(50, len(park_collection.get_park_list()))


if __name__ == '__main__':
    unittest.main()
