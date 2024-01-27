import requests


def weatherData(name):
    api_key = '469078c940e87415b83bd3acfd7c68e8'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    city_name = 'Egham'
    country_code = 'COUNTRY_CODE'

    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}'

    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse and print the weather data
        weather_data = response.json()
        print(weather_data)
    else:
        print(f'Error: {response.status_code}')
