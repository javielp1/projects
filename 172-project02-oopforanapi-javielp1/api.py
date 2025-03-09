import requests
import json

response = requests.get('https://developer.nps.gov/api/v1/activities/parks?api_key=ghfLLz9Mp87UfSTT0OaDzB5hgslXUtug0sgklKoR')
data = response.json()
print(json.dumps(data, indent=4))

