import json
import unittest
from park import Park


class ParkTest(unittest.TestCase):
    def test_get_park(self):
        with open('park_json.json', 'r') as json_file:
            park_data = json.load(json_file)
            first_park_data = park_data['data'][0]
            first_park = Park(first_park_data)
            self.assertEqual(first_park.get_park(), 'Abraham Lincoln Birthplace National Historical Park')

    def test_get_url(self):
        with open('park_json.json') as json_file:
            park_data = json.load(json_file)
            first_park_data = park_data['data'][0]
            first_park = Park(first_park_data)
            self.assertEqual(first_park.get_url(), 'https://www.nps.gov/abli/index.htm')



    def test_get_description(self):
        with open('park_json.json') as json_file:
            park_data = json.load(json_file)
            first_park_data = park_data['data'][0]
            first_park = Park(first_park_data)
            self.assertEqual(first_park.get_description(), "For over a century people from around the world have come "
                                                           "to rural Central Kentucky to honor the humble beginnings "
                                                           "of our 16th president, Abraham Lincoln. His early life on "
                                                           "Kentucky's frontier shaped his character and prepared him "
                                                           "to lead the nation through Civil War. Visit our country's "
                                                           "first memorial to Lincoln, built with donations from "
                                                           "young and old, and the site of his childhood home.")

    def test_get_image_url(self):
        with open('park_json.json') as json_file:
            park_data = json.load(json_file)
            first_park_data = park_data['data'][0]
            first_park = Park(first_park_data)
            self.assertEqual(first_park.get_image_url(),
                             "https://www.nps.gov/common/uploads/structured_data/3C861078-1DD8-B71B-0B774A242EF6A706"
                             ".jpg")


if __name__ == '__main__':
    unittest.main()
