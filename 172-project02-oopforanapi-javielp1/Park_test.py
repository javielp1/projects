import unittest
import json

from park import Park


class TestPark(unittest.TestCase):

    def test_get_url(self):
        with open('park_json.json', 'r',encoding='utf-8') as park_input_file:
            park_data = json.load(park_input_file)
            first_park_json = park_data['data'][0]['parks'][0]
            first_park = Park(first_park_json)
            self.assertEqual(first_park.get_url(), 'https://www.nps.gov/acad/index.htm')
            second_park_json = park_data['data'][0]['parks'][1]
            second_park = Park(second_park_json)
            self.assertEqual(second_park.get_url(), 'https://www.nps.gov/afbg/index.htm')

    def test_get_url_with_park_name(self):
        with open('park_json.json', 'r',encoding='utf-8') as park_input_file:
            park_data = json.load(park_input_file)
            first_park_json = park_data['data'][0]['parks'][0]
            first_park = Park(first_park_json)
            self.assertEqual(first_park.get_url_with_park_name_(), 'https://www.nps.gov/acad/index.htm')



    def test_get_state(self):
        with open('park_json.json', 'r',encoding='utf-8') as park_input_file:
            park_data = json.load(park_input_file)
            first_park_json = park_data['data'][0]['parks'][0]
            first_park = Park(first_park_json)
            self.assertEqual(first_park.get_state(), 'ME')
            second_park_json = park_data['data'][0]['parks'][1]
            second_park = Park(second_park_json)
            self.assertEqual(second_park.get_state(), 'NY')




