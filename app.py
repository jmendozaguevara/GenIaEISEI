import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from utils import conexionBD
import practicaOpenAIconSQL

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'title': 'Bienvenido a Ia Gen Eisei',
        'message': 'Ejemplo de uso de OpenAi con la integracion de Angular, Python'
    }
    response = jsonify(data)
    return response

@app.route('/api/message', methods=['POST'])
def handle_message():
    if request.method == 'POST':
        msg = request.form['message']
        assistant = practicaOpenAIconSQL.OpenAIAssistant(msg)
        answer = assistant.get_response()
        print(answer)
        return jsonify(answer)
    else:
        return jsonify({'response' : 'no se obtuvo mensaje'})

if __name__ == '__main__':
    app.run()