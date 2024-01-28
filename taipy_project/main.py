from taipy import Gui 
from weatherAPI import weatherData, getRecommendations
import time

def weather_pressed(state):
    if state.recommendations[3] != "Default.png":
    	state.dog = state.recommendations[2]
    	state.bg = "static.png"
    	time.sleep(0.3)
    	state.bg = state.recommendations[3]
    	state.dialogue = state.recommendations[4]
    
def clothes_pressed(state):
   if state.recommendations[3] != "Default.png":
    	state.clothes = state.recommendations[0]
    	state.coat = state.recommendations[1]

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.recommendations = getRecommendations(var_value)
		state.value = weatherData(var_value)
		state.degrees = str(state.value[2]) + u'\N{DEGREE SIGN}' + "C"
		print(state.recommendations)

global recommendations, clothes, dog, coat, dialogue, bg
recommendations = [ "", "", "shiba.gif", "Default.png", ""]	

clothes = "empty.png"
dog = "shiba.gif"
coat = "empty.png"
dialogue = "empty.png"
bg = "Default.png"
degrees = ""

places = ["London", "Egham", "Whitton", "Algiers", "Aberdeen", "Mumbai", "Manila", "New York", "Paris", "Cape Town"]

value = [ " "," "," ", " ", " ", " ", " ", " ", " ", " "]

page="""

<|layout|columns=2 2 1 1

<|part|
<br/>
<|container container-selector|
<|{value}|selector|lov={places}|dropdown|label=Select the city|id="select"|>
|>
<|container container-card|
<br/>
<|{value[0]}|> <br/>
<|{value[1]}|> <br/>
<|{degrees}|> <br/>
|>
|>

#

#

<br/>
<|{"shirt.png.png"}|image|height=100px|width=100px|label=Recommendation|on_action=clothes_pressed|id=button|><|{"sun.gif"}|image|height=100px|width=100px|label=Weather|on_action=weather_pressed|id=button|>

#

<|{clothes}|image|height=200px|width=240px|>

<|{coat}|image|height=200px|width=200px|>

#

<|{bg}|image|label=Weather|height=240px|width=400px|>

<|{dog}|image|height=300px|width=300px|label=Shiba|>

<|{dialogue}|image|height=300px|width=520px|label=Words|>

#

#

#

|>
  
"""

if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
