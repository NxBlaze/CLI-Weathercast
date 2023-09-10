from locate import get_coords
from project import convert_date
from weathercodes import get_weather_status


def test_get_coords():
    assert get_coords("Białystok") == {'lat': 53.13248859999999, 'lng': 23.1688403}
    assert get_coords("London") == {'lat': 51.5072178, 'lng': -0.1275862}
    assert get_coords("Cambrige, MA") == {'lat': 42.3736158, 'lng': -71.10973349999999}
    assert get_coords("czumoczunguma") == False


def test_convert_date():
    assert convert_date("2022-07-01T00:00") == "01/07/2022 00:00:00"
    assert convert_date("2023-09-10T13:19") == "10/09/2023 13:19:00"


def test_weather_status():
    assert get_weather_status(0) == "☀️  Clear sky"
    assert get_weather_status(99) == "⛈️⚠️  Thunderstorm, heavy hail"
    assert get_weather_status(100) == "Unknown weather status"