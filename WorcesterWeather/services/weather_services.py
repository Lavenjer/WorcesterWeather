import requests
from datetime import datetime
from WorcesterWeather.models import HourlyWeather

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_hourly_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": [
            "temperature_2m",
            "apparent_temperature",
            "wind_speed_10m",
            "wind_direction_10m",
            "visibility",
            "precipitation_probability"
        ],
        "timezone": "UTC"
    }

    response = requests.get(OPEN_METEO_URL, params=params)
    response.raise_for_status()
    data = response.json()

    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    apparent_temps = data["hourly"]["apparent_temperature"]
    wind_speeds = data["hourly"]["wind_speed_10m"]
    wind_directions = data["hourly"]["wind_direction_10m"]
    visibilities = data["hourly"]["visibility"]
    precipitation_probs = data["hourly"]["precipitation_probability"]

    records = []

    for i in range(len(times)):
        records.append(
            HourlyWeather(
                latitude=lat,
                longitude=lon,
                time=datetime.fromisoformat(times[i]),
                temperature=temperatures[i],
                apparent_temperature=apparent_temps[i],
                wind_speed=wind_speeds[i],
                wind_direction=wind_directions[i],
                visibility=visibilities[i],
                precipitation_probability=precipitation_probs[i],
            )
        )
    HourlyWeather.objects.filter(latitude=lat, longitude=lon).delete()
    HourlyWeather.objects.bulk_create(records, batch_size=50)
    return records