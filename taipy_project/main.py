from taipy import Gui 
from weatherAPI import weatherData

def weather_pressed(state):
    state.message = "Today is cold"
    
def clothes_pressed(state):
    state.message = "You should wear a hat"

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)

message = "Welcome to CKC Weathers"
		
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

Mascot goes here<br/>
Cat: <|{message}|text|><br/>
<|{"cat.png"}|image|height=300px|width=300px|label=Cat|>

Menu goes here
<|{"cat.png"}|image|height=50px|width=50px|label=Reccomendation|on_action=clothes_pressed|><|{"cat.png"}|image|height=50px|width=50px|label=Weather|on_action=weather_pressed|>


|>
  
"""


if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
