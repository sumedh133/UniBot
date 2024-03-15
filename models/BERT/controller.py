import json
import os
import pandas as pd
from transformers import BertForSequenceClassification, BertTokenizerFast, pipeline
import random
dir_path = os.path.dirname(os.path.realpath(__file__))

model_path = os.path.join(dir_path, './bin')
intents = json.loads(open(os.path.join(dir_path, '../../data/intents_generated.json')).read())

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer= BertTokenizerFast.from_pretrained(model_path)
chatbot= pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def create_and_extract_info(json_file):
    df = pd.DataFrame({
        'Pattern' : [],
        'Tag' : []
    })

    for intent in json_file['intents']:
        for pattern in intent['patterns']:
            sentence_tag = [pattern, intent['tag']]
            df.loc[len(df.index)] = sentence_tag

    return df

df = create_and_extract_info(intents)
labels = df['Tag'].unique().tolist()
labels = [s.strip() for s in labels]
label2id = {label:id for id, label in enumerate(labels)}

def get_response(text):
    text = text.strip().lower()
    score = chatbot(text)[0]['score']

    if score < 0.7:
        return "Sorry I can't answer that currently"

    label = label2id[chatbot(text)[0]['label']]
    response = random.choice(intents['intents'][label]['responses'])

    return response

def chatbot_cli():
    print("Chatbot is ready. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot_cli()
