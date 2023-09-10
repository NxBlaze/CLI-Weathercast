import requests
from sys import exit
import timecalc
import locate
import graphs
import weathercodes


def main():
    # Prompt user for location, retry if invalid
    while True:
        adress = input("Location: ")
        if location := locate.get_coords(adress):
            break
        print("Invalid Location")

    weather = get_weather(location)

    # Convert dates in forecast to a format accepted by plotext
    dates = []
    try:
        for date in weather.json()["hourly"]["time"]:
            dates.append(convert_date(date))

        # Grab the datapoints for precipitation, temperature and weathercodes
        precipitation = weather.json()["hourly"]["precipitation_probability"]
        temp = weather.json()["hourly"]["temperature_2m"]
        weathercode = weather.json()["hourly"]["weathercode"]
    except KeyError:
        exit("Hourly weather data for that location is currently unavailable.")

    # Draw weekly graphs for temperature and precipitation chance
    graphs.plot_temp(dates, temp)
    graphs.plot_precipitation(dates, precipitation)

    # Print the current weather
    print(
        f"Current weather for {adress}:", get_current_weather(dates, weathercode, temp)
    )


# Get the forecast for specified location from open-meteo.com
def get_weather(location):
    retries = 0
    while retries < 10:
        try:
            weather = requests.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={location['lat']}&longitude={location['lng']}&hourly=temperature_2m,precipitation_probability,weathercode&timezone=auto",
                timeout=3,
            )
        except requests.exceptions.ReadTimeout:
            retries += 1
            pass
        else:
            return weather

    exit("Weather data unavailable, please try again later")


# Convert open-meteo.com times to format accepted by plotext
def convert_date(date):
    rest, minutes = date.split(":")
    rest, hours = rest.split("T")
    year, month, day = rest.split("-")
    return f"{day}/{month}/{year} {hours}:{minutes}:00"


# Return current weather
def get_current_weather(dates, code, temps):
    for i in range(len(dates)):
        if dates[i] == timecalc.get_current_time():
            weather = weathercodes.get_weather_status(code[i])
            temp = temps[i]
            return f"{weather}, {temp} °C"

    return "Could not parse weather data"


if __name__ == "__main__":
    main()
