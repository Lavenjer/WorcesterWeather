from django.urls import path
from .views import hourly_weather_view, cycling_safety_index

"""
Routes requests to views.py
"""
urlpatterns = [
    path("hourly/", hourly_weather_view, name="hourly-weather"),
    path("safety/", cycling_safety_index, name="cycling-safety")
]