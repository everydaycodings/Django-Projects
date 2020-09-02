import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
# Create your views here.


def index(request):
    
    # API from openweather.org
    web = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=b972c56a95dffde980bd98f9980ca3f0"
    
    err_msg = ""
    message = ""
    message_class = ""
    
    # It checks wearher there is any search for the city
    if request.method == "POST":
        form = CityForm(request.POST)
        
        # It checks that city exits or not
        if form.is_valid():
            new_city = form.cleaned_data["city"]
            existing_city_count =  City.objects.filter(city=new_city).count()
            
            # If city exits in the world it checks where the city exits in database for dublicates 
            if existing_city_count == 0:
                r = requests.get(web.format(new_city)).json()
                if r["cod"] == 200:
                    form.save()
                else:
                    err_msg = "City Doesnot Exit!"
            else:
                err_msg = "City Already Exits in the Website!"
        
        # Messages are shown according to the conditions
        if err_msg:
            message = err_msg
            message_class = "is-danger"
        else:
            message = "City added successfully"
            message_class = "is-success"

    # All the city are fetch from databse in decending order         
    form = CityForm()
    cities = City.objects.all().order_by("-id")
    
    weather_data = []
    
    # All the city datails are fetched from the API one by one
    for city in cities:
        r = requests.get(web.format(city)).json()

        city_weather = {
            "city": city.city,
            "temperature": r["main"]["temp"],
            "humidity": r["main"]["humidity"],
            "desc": r["weather"][0]["description"],
            "wind_speed": r["wind"]["speed"],
            "icon": r["weather"][0]["icon"],
            "lon": r["coord"]["lon"],
            "lat": r["coord"]["lat"],
        }

        weather_data.append(city_weather)

    context = {
        "weathers": weather_data, 
        "form": form,
        "message": message, 
        "message_class": message_class
        }
    
    return render(request, "weather_app/index.html", context)



def delete_city(request, city_name):
    
    # It takes the paticular city_name and delete that city from database
    City.objects.get(city=city_name).delete()

    return redirect("index")