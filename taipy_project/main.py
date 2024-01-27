from taipy import Gui
from weatherAPI import weatherData

# Calls API that prints weather data in JSON format
print(weatherData("Egham"))

Gui(page="Hello *World*").run(use_reloader=True, port=5001)
