from django.contrib import admin
from WorcesterWeather.models import HourlyWeather

@admin.register(HourlyWeather)
class HourlyWeatherAdmin(admin.ModelAdmin):
    list_display = (
        "time",
        "temperature",
        "apparent_temperature",
        "wind_speed",
        "visibility",
        "precipitation_probability",
    )
    ordering = ("-time",)