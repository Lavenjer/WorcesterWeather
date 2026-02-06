from django.db import models

class HourlyWeather(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()
    temperature = models.FloatField()
    apparent_temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.TextField()
    visibility = models.FloatField()
    precipitation_probability = models.FloatField()

    def __str__(self):
        return f"{self.temperature}°F (feels like {self.apparent_temperature}°F) at {self.time}"
