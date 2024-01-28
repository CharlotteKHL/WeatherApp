import requests

# requests data from OpenWeatherMap API
# param: Name of City location
def weatherData(name):
    api_key = '469078c940e87415b83bd3acfd7c68e8'

    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}'

    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse and print the weather data
        weather_data = response.json()

        temp = weather_data['main']
        weather = weather_data['weather'][0]
        weathertype = weather['main']
        temperature = kelvinToCelcius(temp['temp'])

        data = [name, weathertype, temperature]
        return data
    else:
        print(f'Error: {response.status_code}')


def getRecommendations(name):
    data = weatherData(name)
    temp = formatTemp(data[2])

    clothes = []
    weather = data[1]
    Hazard = ["Tornado", "Dust", "Ash", "Squall"] 
    Cloud = ["Clouds", "Fog", "Smoke", "Haze"]
    Precipitation = ["Rain", "Drizzle", "Mist"]
    
    if weather == "Clear":
        if temp < 14:
            clothes.append("coldoutfit.png")
        else:
            clothes.append("warmoutfit.png")
        if temp < 8:
            clothes.append("coat.png")
        else:
            clothes.append("nocoat.png")
            
        if temp >= 14:
            clothes.append("sunnydog.gif")
        else:
            clothes.append("cleardog.gif")
        clothes.append("clearbg.gif")
        clothes.append("cleardialogue.png")
    if weather in Hazard:
        if temp < 14:
            clothes.append("coldoutfit.png")
        else:
            clothes.append("warmoutfit.png")
        if temp < 8:
            clothes.append("coat.png")
        else:
            clothes.append("nocoat.png")
        clothes.append("raindog.gif")
        clothes.append("hazardbg.gif")
        clothes.append("hazarddialogue.png")
    if weather in Cloud:
        if temp < 14:
            clothes.append("coldoutfit.png")
        else:
            clothes.append("warmoutfit.png")
        if temp < 8:
            clothes.append("coat.png")
        else:
            clothes.append("nocoat.png")
        clothes.append("shiba.gif")
        clothes.append("cloudybg.gif")
        clothes.append("cloudydialogue.png")
    if weather in Precipitation:
        if temp < 14:
            clothes.append("coldoutfit.png")
        else:
            clothes.append("warmoutfit.png")
        if temp < 8:
            clothes.append("coat.png")
        else:
            clothes.append("nocoat.png")
        clothes.append("raindog.gif")
        clothes.append("raindbg.gif")
        clothes.append("precipitationdialogue.png")
    elif weather == "Snow": #Snow
        if temp < 14:
            clothes.append("coldoutfit.png")
        else:
            clothes.append("warmoutfit.png")
        if temp < 8:
            clothes.append("coat.png")
        else:
            clothes.append("nocoat.png")
        clothes.append("raindog.gif")
        clothes.append("snowbg.gif")
        clothes.append("snowdialogue.png")
    return clothes

def kelvinToCelcius(num):
    return round(num - 273.15, 2)

def formatTemp(temp):
    print(temp)
    return int(float(temp))
