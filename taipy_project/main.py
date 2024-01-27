from taipy import Gui 
from weatherAPI import weatherData

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)
		
# Calls API that prints weather data in JSON format
print(weatherData("Egham")[1])

places = ["London", "Egham", "Whitton" ]

value = [ "", "", ""]


page="""

<|layout|columns=3 3 1

<{value}|selector|lov={places}|dropdown|on_action=submit_selection|>

Mascot goes here

Menu goes here

<|{value[0]}|>
<|{value[1]}|>
<|{value[2]}|>

|>
  
"""


if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
