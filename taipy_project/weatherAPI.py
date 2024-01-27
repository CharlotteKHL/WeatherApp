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


def kelvinToCelcius(num):
    conversion = round(num - 273.15, 2)
    return str(conversion) + u'\N{DEGREE SIGN}' + "C"
