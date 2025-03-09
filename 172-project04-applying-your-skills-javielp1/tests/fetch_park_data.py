import json
import os


def fetch_park_data_from_file():
    file_path = os.path.join(os.path.dirname(__file__), 'park_json.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
