from django.urls import path
from .views import hourly_weather_view

urlpatterns = [
    path("hourly/", hourly_weather_view, name="hourly-weather"),
]