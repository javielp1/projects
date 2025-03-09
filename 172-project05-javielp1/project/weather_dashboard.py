import requests
import json
import matplotlib.pyplot as plt
from weather_data import WeatherData

class WeatherDashboard:
    """
    Fetches, stores, and processes weather data for multiple cities.
    """
    API_KEY = "c8f34f8e78c89488d17b820d567b98cf"  # Replace with your OpenWeatherMap API key

    def __init__(self):
        self.weather_data_list = []

    def fetch_data(self, city_name):
        """
        Fetch weather data for a city and store it.
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = WeatherData(
                city_name=data['name'],
                temperature=data['main']['temp'],
                humidity=data['main']['humidity'],
                wind_speed=data['wind']['speed']
            )
            self.weather_data_list.append(weather)
            print(f"Weather data for {city_name} added.")
        else:
            print(f"Could not fetch data for {city_name}. Check city name or API key.")

    def save_to_file(self, filename="weather_data.json"):
        """
        Save all weather data to a JSON file. This overwrites any existing file.
        """
        weather_dicts = [
            {
                "city_name": data.city_name,
                "temperature": data.temperature,
                "humidity": data.humidity,
                "wind_speed": data.wind_speed
            }
            for data in self.weather_data_list
        ]
        with open(filename, "w") as file:
            json.dump(weather_dicts, file, indent=4)
        print(f"Weather data saved to {filename}.")

    def display_all(self):
        """
        Displays all weather data stored in memory.
        """
        for weather in self.weather_data_list:
            print(weather.display())

    def sort_by_temperature(self):
        """
        Sort the list of weather data by temperature.
        """
        self.weather_data_list.sort(key=lambda x: x.temperature)

    def plot_data(self):
        """
        Plot temperature data for the cities in a bar graph.
        """
        cities = [data.city_name for data in self.weather_data_list]
        temps = [data.temperature for data in self.weather_data_list]

        plt.bar(cities, temps)
        plt.xlabel("Cities")
        plt.ylabel("Temperature (°C)")
        plt.title("City Temperatures")
        plt.show()
