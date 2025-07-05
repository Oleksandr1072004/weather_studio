from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.conf import settings
import datetime
import json
import requests

api_key = settings.OPENWEATHER_API_KEY

current_link = "http://api.openweathermap.org/data/2.5/weather?g="
city_name = ""


# Create your views here.
def index(request):
    return render(request, "weather_app/index.html")


def convert_calvin_to_celcius(degree):
    return degree - 273.15


def convert_calvin_to_farenheit(degree):
    fahrenheit = (degree - 273.15) * 9 / 5 + 32
    return fahrenheit


def get_city(request):
    global city_name
    query_dict = request.GET
    query = query_dict.get("search")

    if not query or not query.strip():
        return render(request, "weather_app/error.html", {
            'error': 'Please enter a valid city name'
        })

    try:
        full_info = f"http://api.openweathermap.org/data/2.5/weather?q={query.strip()}&appid={api_key}"
        r = requests.get(full_info)
        r.raise_for_status()  # Raise exception for HTTP errors
        data = r.json()

        if data.get('cod') != 200:
            return render(request, "weather_app/error.html", {
                'error': data.get('message', 'Unknown error from weather API')
            })

        context = {
            'city_name': data["name"],
            'country': data["sys"]["country"],
            'current_time': datetime.datetime.now().strftime(
                "%d.%m.%Y %H:%M:%S"),
            'temp': "{0:.2f}".format(data["main"]["temp"]),
            'feels_like': "{0:.2f}".format(data["main"]["feels_like"]),
            'temp_min': "{0:.2f}".format(data["main"]["temp_min"]),
            'temp_max': "{0:.2f}".format(data["main"]["temp_max"]),
            'humidity': data["main"]["humidity"],
            'wind_speed': data["wind"]["speed"],
            'weather_desc': data["weather"][0]["main"],
        }
        city_name = data["name"]
        print("City name:", city_name)
        return render(request, "weather_app/detail.html", context)

    except requests.exceptions.RequestException as e:
        return render(request, "weather_app/error.html", {
            'error': f'Failed to connect to weather service: {str(e)}'
        })
    except (KeyError, ValueError) as e:
        return render(request, "weather_app/error.html", {
            'error': 'Invalid data received from weather service'
        })


def get_city_celcius(request):
    global city_name
    full_info = f"http://api.openweathermap.org/data/2.5/weather?q={city_name.strip()}&appid={api_key}"
    r = requests.get(full_info)
    r.raise_for_status()  # Raise exception for HTTP errors
    data = r.json()
    context = {
        'city_name': data["name"],
        'country': data["sys"]["country"],
        'current_time': datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M:%S"),
        'temp': "{0:.2f}".format(convert_calvin_to_celcius(data["main"]["temp"])),
        'feels_like': "{0:.2f}".format(
            convert_calvin_to_celcius(data["main"]["feels_like"])),
        'temp_min': "{0:.2f}".format(
            convert_calvin_to_celcius(data["main"]["temp_min"])),
        'temp_max': "{0:.2f}".format(
            convert_calvin_to_celcius(data["main"]["temp_max"])),
        'humidity': data["main"]["humidity"],
        'wind_speed': data["wind"]["speed"],
        'weather_desc': data["weather"][0]["main"],
    }

    return render(request, "weather_app/detail.html", context)


def get_city_farenheit(request):
    global city_name
    full_info = f"http://api.openweathermap.org/data/2.5/weather?q={city_name.strip()}&appid={api_key}"
    r = requests.get(full_info)
    r.raise_for_status()  # Raise exception for HTTP errors
    data = r.json()

    if data.get('cod') != 200:
        return render(request, "weather_app/error.html", {
            'error': data.get('message', 'Unknown error from weather API')
        })

    context = {
        'city_name': data["name"],
        'country': data["sys"]["country"],
        'current_time': datetime.datetime.now().strftime(
            "%d.%m.%Y %H:%M:%S"),
        'temp': "{0:.2f}".format(convert_calvin_to_farenheit(data["main"]["temp"])),
        'feels_like': "{0:.2f}".format(
            convert_calvin_to_farenheit(data["main"]["feels_like"])),
        'temp_min': "{0:.2f}".format(convert_calvin_to_farenheit(data["main"]["temp_min"])),
        'temp_max': "{0:.2f}".format(convert_calvin_to_farenheit(data["main"]["temp_max"])),
        'humidity': data["main"]["humidity"],
        'wind_speed': data["wind"]["speed"],
        'weather_desc': data["weather"][0]["main"],
    }

    return render(request, "weather_app/detail.html", context)
