from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import utils
from .models import Country, City
import datetime
import json
import geopandas
import pandas as pd
import requests
import time

openweather_api = "eb890cd5bf4c9f09d0a947f4f21dac8a"

# current_link = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
current_link = "http://api.openweathermap.org/data/2.5/weather?g="


# Create your views here.
def index(request):
    country = Country.objects.all()
    city = Country.objects.all()
    # return HttpResponse("index.html")
    city_name = "Chernivtsi"
    full_info = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={openweather_api}"
    # for subject in full_info:
    #     print(subject)
    r = requests.get(full_info)
    print(requests.get(full_info))
    data = r.json()
    info = f"""
            Name of your city: {city_name}
            Datetime Now: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}
            Current Temperature: {data["main"]["temp"]}
            Feels like: {data["main"]["feels_like"]}
            Minimum temperature: {data["main"]["temp_min"]}
            Maximum temperature: {data["main"]["temp_max"]}
            Humidity: {data["main"]["humidity"]}
            Wind speed: {data["wind"]["speed"]}
            Country of your city: {data["sys"]["country"]}
            Weather meaning: {data["weather"][0]["main"]}
            """
    print(info)
    return render(request, "weather_app/index.html")


def get_city(request):
    query_dict = request.GET
    query = query_dict.get("search")
    print(query)

    full_info = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={openweather_api}"
    r = requests.get(full_info)
    data = r.json()

    context = {
        'city_name': data["name"],
        'country': data["sys"]["country"],
        'current_time': datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        'temp': data["main"]["temp"],
        'feels_like': data["main"]["feels_like"],
        'temp_min': data["main"]["temp_min"],
        'temp_max': data["main"]["temp_max"],
        'humidity': data["main"]["humidity"],
        'wind_speed': data["wind"]["speed"],
        'weather_desc': data["weather"][0]["main"],
    }

    return render(request, "weather_app/detail.html", context)