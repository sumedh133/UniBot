import json

with open("data/intents.json","r") as file:
    intents_data=json.load(file)

intents=[]
for x in intents_data['intents']:
    print(f"{x['tag']}:{x['responses']}")
    