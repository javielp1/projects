from park import Park
import json


class ParkCollection:
    def __init__(self, park_json):
        self.park_list = []

        for park in park_json:
            self.park_list.append(Park(park))

    def get_park_list(self):
        return self.park_list
