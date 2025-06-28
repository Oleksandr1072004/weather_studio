from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
import datetime
import json
import requests

api_key = "eb890cd5bf4c9f09d0a947f4f21dac8a"

current_link = "http://api.openweathermap.org/data/2.5/weather?g="


# Create your views here.
def index(request):
    return render(request, "weather_app/index.html")


def get_city(request):
    query_dict = request.GET
    query = query_dict.get("search")
    print(query)
    print("Type:",type(query))
    try:
        full_info = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}"
        r = requests.get(full_info)
        data = r.json()

        try:
            context = {
                'city_name': data["name"],
                'country': data["sys"]["country"],
                'current_time': datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                'temp': "{0:.2f}".format(data["main"]["temp"] - 273.15),
                'feels_like': "{0:.2f}".format(data["main"]["feels_like"] - 273.15),
                'temp_min': "{0:.2f}".format(data["main"]["temp_min"] - 273.15),
                'temp_max': "{0:.2f}".format(data["main"]["temp_max"] - 273.15),
                'humidity': data["main"]["humidity"],
                'wind_speed': data["wind"]["speed"],
                'weather_desc': data["weather"][0]["main"],
            }

            return render(request, "weather_app/detail.html", context)
        except KeyError or AttributeError:
            return "There are some error"
    except ValueError or KeyError or AttributeError:
        return "There are some errors"
