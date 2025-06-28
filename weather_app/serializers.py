from rest_framework import serializers


class Country(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    datetime_now = serializers.DateTimeField()
    current_temperature = serializers.FloatField()
    feeling_like = serializers.FloatField()
    minimum_temperature = serializers.FloatField()
    maximum_temperature = serializers.FloatField()
    humidity = serializers.IntegerField()
    wind_speed = serializers.FloatField()
    weather_meaning = serializers.CharField(max_length=200)


class City(serializers.Serializer):
    city_name = serializers.CharField(max_length=300)
