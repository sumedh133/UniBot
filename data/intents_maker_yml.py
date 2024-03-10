import yaml
import json

def convert_json_to_nlu_yaml(json_file):
    with open("data/augmented_intents.json", 'r') as file:
        data = json.load(file)

    nlu_data = {'version': '3.1', 'nlu': []}

    for intent in data['intents']:
        # Use a multiline scalar block for 'examples'
         # Add more lines if needed
        x=" | \n-"
        for t in intent['patterns']:
            x+=t
            x+="\n-"
        nlu_data['nlu'].append({"intent": intent["tag"], "examples": x})

        # nlu_data['nlu'].append({"intent": intent["tag"], "examples": f" |-\n  {repr(intent['patterns'])}"})


    yaml_output = yaml.dump(nlu_data, default_flow_style=False)

    with open('nlu.yml', 'w') as output_file:
        output_file.write(yaml_output)

if __name__ == "__main__":
    convert_json_to_nlu_yaml('intents.json')
