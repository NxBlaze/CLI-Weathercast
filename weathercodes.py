code = {
    0: "☀️  Clear sky",
    1: "🌤️  Mainly clear",
    2: "🌥️  Partly cloudy",
    3: "☁️  Overcast",
    45: "🌫️  Fog",
    48: "🌫️  Fog, depositing rime",
    51: "🌦️  Light drizzle",
    53: "🌦️  Moderate drizzle",
    55: "🌦️  Dense drizzle",
    56: "🌦️❄️  Freezing drizzle, light",
    57: "🌦️❄️  Freezing drizzle, dense",
    61: "🌧️  Slight rain",
    63: "🌧️  Moderate rain",
    65: "🌧️  Heavy rain",
    66: "🌧️❄️  Freezing rain, light",
    67: "🌧️❄️  Freezing rain, heavy",
    71: "🌨️  Slight snowfall",
    73: "🌨️  Moderate snowfall",
    75: "🌨️⚠️  Heavy snowfall",
    77: "🌨️  Snow grains",
    80: "⛆  Slight rain showers",
    81: "⛆  Moderate rain showers",
    82: "⛆⚠️  Violent rain showers",
    85: "🌨️  Slight snow showes",
    86: "🌨️⚠️  Heavy snow showers",
    95: "⛈️⚠️  Thunderstorm",
    96: "⛈️⚠️  Thunderstorm, slight hail",
    99: "⛈️⚠️  Thunderstorm, heavy hail"

}


# Interpret weathercode and return proper weather string
def get_weather_status(n):
    if n in code:
        return code[n]
    else:
        return "Unknown weather status"