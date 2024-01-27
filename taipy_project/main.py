from taipy import Gui
from weatherAPI import weatherData

# Calls API that prints weather data in JSON format
print(weatherData("Egham"))

places = [ "London", "Egham", "Whitton" ]

value = "Pick a city :D"



page="""

<|layout|columns=3 3 1

<|{value}|selector|lov={places}|dropdown|>

Mascot goes here

Menu goes here

<|{value}|>

|>
  
"""


if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
