class WeatherData:
    """
    Represents weather data for a single city.
    """
    def __init__(self, city_name, temperature, humidity, wind_speed):
        self.city_name = city_name
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def display(self):
        """
        Returns a string representation of the weather details.
        """
        return f"{self.city_name} - Temp: {self.temperature}°C, Humidity: {self.humidity}%, Wind Speed: {self.wind_speed} km/h"
