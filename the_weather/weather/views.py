from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def index(request):
    url =  'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5cfa51d7dcc19f20d6713ec7e37133d2'
    
    cities = City.objects.all() # return all cities in the database
    
    if request.method == 'POST': #only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validated

    form = CityForm()
    weather_data = []
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) 
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context)  #returns the index.html template asdad