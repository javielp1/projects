import unittest
from weather_data import WeatherData
from weather_dashboard import WeatherDashboard

class TestWeatherDashboard(unittest.TestCase):

    def test_weather_data_display(self):
        weather = WeatherData("Test City", 25, 50, 10)
        self.assertEqual(weather.display(), "Test City - Temp: 25°C, Humidity: 50%, Wind Speed: 10 km/h")

    def test_sorting(self):
        dashboard = WeatherDashboard()
        dashboard.weather_data_list = [
            WeatherData("City A", 30, 40, 5),
            WeatherData("City B", 20, 60, 7),
            WeatherData("City C", 25, 55, 10)
        ]
        dashboard.sort_by_temperature()
        self.assertEqual([city.city_name for city in dashboard.weather_data_list], ["City B", "City C", "City A"])

if __name__ == '__main__':
    unittest.main()
