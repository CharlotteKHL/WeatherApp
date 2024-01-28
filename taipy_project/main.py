from taipy import Gui 
from weatherAPI import weatherData, getRecommendations

def weather_pressed(state):
    state.message = "Today is cold"
    
def clothes_pressed(state):
    state.message = "You should wear a hat"

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)
		state.recommendations = getRecommendations(var_value)

recommendations = []	

message = "Welcome to CKC Weathers"

places = ["London", "Egham", "Whitton" ]


value = [ " "," "," "]

page="""

<|layout|columns=1 2 1

<|part|
<br/>
<|container container-selector|
<|{value}|selector|lov={places}|dropdown|label=Select the city|id="select"|>
|>
<|container container-card|
<br/>
<|{value[0]}|> <br/>
<|{value[1]}|> <br/>
<|{value[2]}|> <br/>
<|{recommendations[0]}|> <br/>
<|{recommendations[1]}|> <br/>
<|{recommendations[2]}|> <br/>
<|{recommendations[3]}|> 
|>
|>

Shiba: <|{message}|text|><br/>

<br/>
<|{"shirt.png.png"}|image|height=100px|width=100px|label=Reccomendation|on_action=clothes_pressed|id=button|><|{"sun.gif"}|image|height=100px|width=100px|label=Weather|on_action=weather_pressed|id=button|>

#

#

#

#

#

#

#

<|{"Shiba.png.gif"}|image|height=300px|width=300px|label=Shiba|>

#

#

#

|>
  
"""

if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
