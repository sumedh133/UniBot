from keras.models import load_model
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import numpy as np
import random
import json
import pickle
import nltk
nltk.download('punkt')
nltk.data.path.append(os.path.join(dir_path, 'packages'))
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

model = load_model(os.path.join(dir_path, 'bin', 'model.h5'))
intents = json.loads(open(os.path.join(dir_path, '../../data/augmented_intents.json')).read())
words = pickle.load(open(os.path.join(dir_path, 'bin', 'words.pkl'),'rb'))
classes = pickle.load(open(os.path.join(dir_path, 'bin', 'classes.pkl'),'rb'))

def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def classify(sentence, model):
    sentence_words = clean_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    p = np.array([bag])
    res = model.predict(p)[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def respond(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def get_response(text):
    ints = classify(text, model)
    res = respond(ints, intents)
    return res

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