from flask import Flask, request, jsonify
from models.NLTK_1.controller import get_response as get_response_nltk
from models.BERT.controller import get_response as get_response_bert
from models.HYBRID.controller import get_response as get_response_hybrid
from models.HYBRID.controller import con as con
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/NLTK_1', methods=['POST'])
def get_nltk_response():
    data = request.json
    message = data.get('message')
    response = get_response_nltk(message)
    if "Mind Reader" in response:   
        response=response.replace("Mind Reader","Unibot")
    return jsonify(response=response)

@app.route('/HYBRID', methods=['POST'])
def get_hybrid_response():
    data = request.json
    message = data.get('message')
    user=data.get('sender')
    contexts=con()
    response = get_response_hybrid(message,user)
    return jsonify(response=response,context=contexts)

@app.route('/BERT', methods=['POST'])
def get_bert_response():
    data = request.json
    message = data.get('message')
    response = get_response_bert(message)
    return jsonify(response=response) 

if __name__ == '__main__':
    app.run(debug=True)  
