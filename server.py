from flask import Flask, request, jsonify
from models.NLTK_1.controller import get_response as get_response_nltk
from models.BERT.controller import get_response as get_response_bert

app = Flask(__name__)

@app.route('/NLTK_1', methods=['GET'])
def get_nltk_response():
    message = request.args.get('message')
    response = get_response_nltk(message)
    return jsonify(response=response)

@app.route('/BERT', methods=['GET'])
def get_bert_response():
    message = request.args.get('message')
    response = get_response_bert(message)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)