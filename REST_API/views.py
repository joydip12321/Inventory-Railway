from django.shortcuts import render
import requests, datetime

def index(request):
    city = request.GET.get("city", "Dhaka")
    url = "https://weather-api138.p.rapidapi.com/weather"

    querystring = {"city_name": city}

    headers = {
        "x-rapidapi-key": "7299415ebemsh0c8591b5f4e8667p1ecc7bjsn636306efb4f3",
        "x-rapidapi-host": "weather-api138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        if 'weather' in data and 'main' in data:
            date = datetime.date.today()
            temperature_celsius = round(data['main']['temp'] - 273.15, 2)

            payload = {
                'city': data['name'],
                'weather': data['weather'][0]['main'],
                'icon': data['weather'][0]['icon'],
                'celcius': temperature_celsius,
                'description': data['weather'][0]['description'],
                'date': date,
            }

            icon_code = data['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_code}.png"

            context = {
                'data': payload,
                'icon_url': icon_url,
                'error': None,
            }
        else:
            context = {
                'data': None,
                'icon_url': "",
                'error': f"City '{city}' not found. Please enter a valid city name.",
            }
    else:
        context = {
            'data': None,
            'icon_url': "",
            'error': "Unable to fetch weather data. Please try again later.",
        }

    return render(request, "weather.html", context)
