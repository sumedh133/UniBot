from flask import Flask, request, jsonify
from models.NLTK_1.controller import get_response

app = Flask(__name__)

@app.route('/NLTK_1', methods=['GET'])
def get_chatbot_response():
    message = request.args.get('message')
    response = get_response(message)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)