from taipy import Gui 
from weatherAPI import weatherData, getRecommendations

def weather_pressed(state):
    state.dog = state.recommendations[2]
    state.bg = state.recommendations[3]
    state.dialogue = state.recommendations[4]
    
def clothes_pressed(state):
    state.clothes = state.recommendations[0]
    state.coat = state.recommendations[1]

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)
		state.recommendations = getRecommendations(var_value)
		print(state.recommendations)

global recommendations, clothes, dog, coat, dialogue, bg
recommendations = [ "", "", "shiba.gif", "Default.png", ""]	

clothes = "empty.png"
dog = "shiba.gif"
coat = "empty.png"
dialogue = "empty.png"
bg = "Default.png"

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
|>
|>

#

<br/>
<|{"shirt.png.png"}|image|height=100px|width=100px|label=Recommendation|on_action=clothes_pressed|id=button|><|{"sun.gif"}|image|height=100px|width=100px|label=Weather|on_action=weather_pressed|id=button|>

#

#

#

#

<|{clothes}|image|label=Clothes|>

<|{coat}|image|label=To coat|>

<|{bg}|image|label=Weather|>

<|{dog}|image|height=300px|width=300px|label=Shiba|>

<|{dialogue}|image|label=Words|>

#

#

|>
  
"""

if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
