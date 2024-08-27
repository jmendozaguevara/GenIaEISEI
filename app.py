import os
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import json
from utils import conexionBD
import openAIconSQL
import Agente_RAG_con_ambiente_local
import base64
import io
import requests
from IPython.display import Image

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'title': 'Bienvenido al curso IA Gen Eisei',
        'message': 'Ejemplos de uso de OpenAi con la integracion de Angular, Python'
    }
    response = jsonify(data)
    return response

@app.route('/api/message', methods=['POST'])
def handle_message():
    if request.method == 'POST':
        msg = request.form['message']
        assistant = openAIconSQL.OpenAIAssistant(msg)
        answer = assistant.get_response()
        print(answer)
        return jsonify(answer)
    else:
        return jsonify({'response' : 'no se obtuvo mensaje'})

##test de display(Image(custom_graph.get_graph(xray=True).draw_mermaid_png()))
#@app.route('/api/agente_rag', methods=['POST'])
#def handle_agenteRag():
#    if request.method == 'POST':
#        msg = request.form['message']
#        print(msg)
#        assistant = Agente_RAG_con_ambiente_local.get_response()
#        return send_file(io.BytesIO(assistant), mimetype='image/png', as_attachment=True, download_name='%s.png' % msg)
#    else:
#        return jsonify({'response' : 'no se obtuvo imagen'})
    
@app.route('/api/agente_rag', methods=['POST'])
def handle_agenteRag():
    if request.method == 'POST':
        msg = request.form['message']
        print(msg)
        assistant = Agente_RAG_con_ambiente_local.get_response(msg)
        return jsonify(assistant)
    else:
        return jsonify({'response' : 'no se obtuvo imagen'})

if __name__ == '__main__':
    app.run()
    