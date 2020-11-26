from django.shortcuts import render, redirect
from .models import City
import os
import requests
import json
from django.contrib.auth.decorators import login_required

def home(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=fr&units=metric&appid={}'
    weather_data = []
    for city in cities :
        city_weather = requests.get(url.format(city, os.getenv('API_KEY'))).json() #request the API data and convert the JSON to Python data types
        weather = {
        'id' : city.id,
        'city' : city_weather['name'],
        'temperature' : city_weather['main']['temp'],
        'ressentie' : city_weather['main']['feels_like'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        }
        weather_data.append(weather)
        
    context = {'weather_data' : weather_data}

    return render(request, 'home.html', context) #returns the home.html template

def add(request):
    req = request.POST.get('search').title()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=fr&units=metric&appid={}'
    city_weather = requests.get(url.format(req, os.getenv('API_KEY'))).json()
    test = city_weather['cod']
    verify = City.objects.filter(name=req)
    
    if test == '404':
        return redirect('weather:home')
    elif test != '404' and not verify:
            new_city = City(name=req)
            new_city.save()

    return redirect('weather:home')

def delete(request):
    if request.method == "POST":
        city_id = request.POST.get('city_id')
        city = City.objects.get(id=city_id)
        city.delete()

    return redirect('weather:home')
