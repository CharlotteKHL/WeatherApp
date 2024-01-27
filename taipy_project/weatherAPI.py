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
            clothes.append("long sleeve")
            clothes.append("trousers")
        if temp >= 14:
            clothes.append("short sleeve")
            clothes.append("shorts")
        if temp < 8:
            clothes.append("coat")
        clothes.append("cap")
        if temp >= 14:
            weather = ["sunglasses", "sunscreen"]
    if weather in Hazard:
        if temp < 14:
            clothes.append("long sleeve")
            clothes.append("trousers")
        if temp >= 14:
            clothes.append("short sleeve")
            clothes.append("shorts")
        elif temp < 8:
            clothes.append("coat")
        clothes.append("No")
    if weather in Cloud:
        if temp < 14:
            clothes.append("long sleeve")
            clothes.append("trousers")
        if temp >= 14:
            clothes.append("short sleeve")
            clothes.append("shorts")
        elif temp < 8:
            clothes.append("coat")
        clothes.append("Default")
    if weather in Precipitation:
        if temp < 14:
            clothes.append("long sleeve")
            clothes.append("trousers")
        if temp >= 14:
            clothes.append("short sleeve")
            clothes.append("shorts")
        elif temp < 8:
            clothes.append("coat")
        clothes.append("Umbrella", "Beanie")
    elif weather == "Snow": #Snow
        if temp < 14:
            clothes.append("long sleeve")
            clothes.append("trousers")
        if temp >= 14:
            clothes.append("short sleeve")
            clothes.append("shorts")
        elif temp < 8:
            clothes.append("coat")
        clothes.append("Beanie")
    
    return clothes

def kelvinToCelcius(num):
    return round(num - 273.15, 2)

def formatTemp(temp):
    print(temp)
    return int(float(temp))
