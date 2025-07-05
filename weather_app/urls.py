from django.urls import path
from . import views

app_name = "weather_app"

urlpatterns = [
    path("", views.index, name='index'),
    path("get_city/", views.get_city, name='detail'),
    path("get_city_celcius/", views.get_city_celcius, name='detail_celcius'),
    path("get_city_farenheit/", views.get_city_farenheit, name='detail_farenheit'),
]
