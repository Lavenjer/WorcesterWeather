from django.shortcuts import render
from WorcesterWeather.services.weather_services import fetch_hourly_weather
from WorcesterWeather.models import HourlyWeather

def hourly_weather_view(request):
    lat = 42.2626
    lon = -71.8023

    # Fetch & store new data (you may later cache this)
    fetch_hourly_weather(lat, lon)

    # Read from database (this is what your app uses)
    weather_data = (
        HourlyWeather.objects
        .filter(latitude=lat, longitude=lon)
        .order_by("time")[24:]
    )

    return render(
        request,
        "HomePage.html",
        {"weather_data": weather_data}
    )