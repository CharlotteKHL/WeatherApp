from taipy import Gui 
from weatherAPI import weatherData, getRecommendations

def weather_pressed(state):
    state.dog = recommendations[2]
    state.bg = recommendations[3]
    state.dialogue = recommendations[4]
    
def clothes_pressed(state):
    state.clothes = recommendations[0]
    state.coat = recommendations[1]

def on_change(state, var_name, var_value):
	if var_name == "value":
		state.value = weatherData(var_value)
		state.recommendations = getRecommendations(var_value)
		print(state.recommendations)

global recommendations, clothes, dog, coat, dialogue, bg
recommendations = [ "", "", "shiba.gif", "Default.png", ""]	

clothes = ""
dog = "shiba.gif"
coat = ""
dialogue = ""
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

Shiba: <|{message}|text|><br/>

<br/>
<|{"shirt.png.png"}|image|height=100px|width=100px|label=Recommendation|on_action=clothes_pressed|id=button|><|{"sun.gif"}|image|height=100px|width=100px|label=Weather|on_action=weather_pressed|id=button|>

#

#

#

#

<|{outfit}|image|height=300px|width=300px|label=Clothes|>

<|{coat}|image|height=300px|width=300px|label=To coat|>

<|{bg}|image|label=Weather|>

<|{dog}|image|height=300px|width=300px|label=Shiba|>

<|{dialogue}|image|height=300px|width=300px|label=Words|>

#

#

|>
  
"""

if __name__ == "__main__":
	Gui(page).run(use_reloader=True, port=5001)
