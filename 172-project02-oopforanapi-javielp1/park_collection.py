from park import Park
import json


class ParkCollection:
    def __init__(self, collection_title, park_json):
        self.collection_title = collection_title
        self.park_json = park_json['data']


    def get_parks_by_state(self, state):
        parks_in_state = []
        for item in self.park_json:
            for park in item['parks']:
                if park.get('states') == state:
                    parks_in_state.append(park)

        return len(parks_in_state)

    def get_parks_with_activities(self, activity):
        pass

    def get_collection_data(self):
        pass
