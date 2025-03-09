from flask import Flask, render_template, request
from park_collection import ParkCollection
from tests.fetch_park_data import fetch_park_data_from_file

app = Flask(__name__)

park_data = fetch_park_data_from_file()

park_collection = ParkCollection(park_data['data'])


@app.route('/')
def home():
    return render_template('home.html', parks=park_collection.get_park_list())


@app.route('/park_info', methods=["GET"])
def view_park_data():
    park_name = request.args.get('park')
    park = next((park for park in park_collection.get_park_list() if park.get_park() == park_name), None)
    return render_template('parks.html', park=park)


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
