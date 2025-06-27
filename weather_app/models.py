from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    datetime_now = models.DateTimeField()
    current_temperature = models.FloatField()
    feeling_like = models.FloatField()
    minimum_temperature = models.FloatField()
    maximum_temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    weather_meaning = models.CharField(max_length=200)


class City(models.Model):
    city_name = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)