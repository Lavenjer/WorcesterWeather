from django.db import models

class HourlyWeather(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()
    temperature = models.FloatField()
    apparent_temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    visibility = models.FloatField()
    precipitation_probability = models.FloatField()

    def __str__(self):
        return f"{self.temperature}°C (feels like {self.apparent_temperature}°C) at {self.time}"
