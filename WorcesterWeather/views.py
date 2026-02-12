from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from WorcesterWeather.models import HourlyWeather

"""
Handles user input and the models to template. It recieves HTTP requests and reads the query's parameters.
The date range is computed and filters the database. Finally, the data is passed onto the template.
"""
def hourly_weather_view(request):

    #Although redundant, this is useful for repopulating the model during development.
    lat = 42.2626
    lon = -71.8023

    day = int(request.GET.get("day", 0))
    day = max(0, min(day, 6))

    start = (
        timezone.localtime()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        + timedelta(days=day)
    )
    end = start + timedelta(days=1)

    weather_data = (
        HourlyWeather.objects
        .filter(
            time__gte=start,
            time__lt=end
        )
        .order_by("time")
    )

    return render(
        request,
        "HomePage.html",
        {
            "weather_data": weather_data,
            "day": day
        }
    )

def cycling_safety_index(request):
    return render(
        request,
        "askdj.html"
    )