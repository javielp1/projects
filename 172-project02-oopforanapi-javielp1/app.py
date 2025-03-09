from flask import Flask, jsonify
import json


app = Flask(__name__)

# Load the park data from JSON file with error handling
try:
    with open("park_json.json", "r") as f:
        park_data = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError("The file 'park_json.json' was not found in the directory.")
except json.JSONDecodeError:
    raise ValueError("The file 'park_json.json' contains invalid JSON.")

def get_all_parks():
    """Extract all parks from the JSON file."""
    parks = []
    for category in park_data["data"]:
        parks.extend(category["parks"])
    return parks

@app.route("/", methods=["GET"])
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Parks API</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #2c3e50; }
            a { display: block; margin: 10px; padding: 10px; background: #3498db; color: white; text-decoration: none; width: 200px; margin: auto; border-radius: 5px; }
            a:hover { background: #2980b9; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Parks API</h1>
        <p>Use the links below to explore the API:</p>
        <a href="/parks">View All Parks</a>
        <a href="/parks/CA">View Parks in California</a>
        <a href="/parks/code/yose">View Yosemite Park</a>
    </body>
    </html>
    '''

@app.route("/parks", methods=["GET"])
def get_parks():
    """Return all parks."""
    return jsonify(get_all_parks())

@app.route("/parks/<state>", methods=["GET"])
def get_parks_by_state(state):
    """Return parks filtered by state."""
    filtered_parks = [park for park in get_all_parks() if state.upper() in park["states"].split(",")]
    return jsonify(filtered_parks)

@app.route("/parks/code/<park_code>", methods=["GET"])
def get_park_by_code(park_code):
    """Return a specific park by its park code."""
    park = next((park for park in get_all_parks() if park["parkCode"].lower() == park_code.lower()), None)
    if park:
        return jsonify(park)
    return jsonify({"error": "Park not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)