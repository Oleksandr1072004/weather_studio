from django.urls import path
from . import views

app_name = "weather_app"

urlpatterns = [
    path("", views.index, name='index'),
    path("get_city/", views.get_city, name='detail'),
]
