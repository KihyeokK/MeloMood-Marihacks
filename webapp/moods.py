from flask import Blueprint, render_template, request
import requests
import os

moods = Blueprint("moods", __name__) #blueprint to be registered
API_KEY = os.environ.get("API_KEY") #envrionment variable for confidential api key

@moods.route('/', methods=["GET", "POST"]) #main route
def mainpage():
    possible_weathers = ['Clear','Clouds', 'Rain', 'Wind', 'Snow'] #possible weathers
 
    if request.method == "POST":
        city = request.form.get('city')
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    

        response = requests.get(URL).json()
        if response["cod"] == "404": #If the city is not valid
            return render_template("error.html")

        weather = response['weather'][0]['main'] #finding weather from reutrned json
        
        for option in possible_weathers:
            if option == weather: #Rendering different templates based on weather
                if weather == 'Clear':
                    return render_template("sunny.html", city=city)
                elif weather == 'Clouds':
                    return render_template("cloudy.html", city=city)
                elif weather == 'Rain':
                    return render_template("rainy.html", city=city)
                elif weather == 'Wind':
                    return render_template("windy.html", city=city)
                elif weather == 'Snow':
                    return render_template("snowy.html", city=city)

    else: #Just in case weathers don't match at all
        return render_template("Home.html")




