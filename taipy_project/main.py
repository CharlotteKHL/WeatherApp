from taipy import Gui 
from weatherAPI import weatherData

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)
		
# Calls API that prints weather data in JSON format
print(weatherData("Egham")[1])

places = ["London", "Egham", "Whitton" ]

value = [ " "," "," "]

page="""

<|layout|columns=3 3 1

<|container|
<br/> <|{value}|selector|lov={places}|dropdown|label=Select the city|>
<|{value[0]}|> <br/>
<|{value[1]}|> <br/>
<|{value[2]}|> <br/>
|>

Mascot goes here

Menu goes here

|>
  
"""


if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
