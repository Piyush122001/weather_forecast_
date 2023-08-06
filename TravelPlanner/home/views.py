from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.TravelPlanner import TravelPlanner
from pprint import pprint 

# Create your views here.

from django.shortcuts import render, redirect
from django.http import JsonResponse

ipdata_key      = "9b1ec21cda46826ff23711bd0507b390d14a2506432ab15e351e9629"
openai_key      = "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"
openweather_key = "8952bcd6d3eea27abe4dd9fdabc1d03c"

def index(request):
    if request.method == 'POST':
        user_input = request.POST['user_prompt']
        # Creating an object of the TravelPlanner class and extracting the information
        planner = TravelPlanner(user_input, ipdata_key, openai_key, openweather_key)
        planner.extract_information()

        # Getting the weather data and printing it
        weather_data, source, destination = planner.get_weather()
        return render(request, 'index.html', {"data": weather_data, "source": source, "destination": destination})

    return render(request, 'index.html')

def signup(request):
    return render(request, "signup.html")

