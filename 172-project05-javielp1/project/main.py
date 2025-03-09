from weather_dashboard import WeatherDashboard

def main():
    dashboard = WeatherDashboard()

    print("Welcome to the Weather Dashboard!")
    while True:
        city = input("Enter a city name (or 'done' to finish): ").strip()
        if city.lower() == 'done':
            break
        dashboard.fetch_data(city)

    print("\nWeather Data:")
    dashboard.display_all()

    print("\nSaving weather data to a file...")
    dashboard.save_to_file()  # Save to JSON file

    print("\nSorting data by temperature...")
    dashboard.sort_by_temperature()
    dashboard.display_all()

    print("\nDisplaying temperature graph...")
    dashboard.plot_data()

if __name__ == "__main__":
    main()
