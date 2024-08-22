import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from utils import conexionBD

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'title': 'Bienvenido a Ia Gen Eisei',
        'message': 'Ejemplo de uso de OpenAi con la integracion de Angular, Python'
    }
    response = jsonify(data)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/message', methods=['POST'])
def handle_message():
    if request.method == 'POST':
        username = request.form['message']
        print(username)
        #ejecutar store con parametros
        params = (1)
        result = conexionBD.execute_sql_storeProcedure("exec F_ObtenEmpresasPorId @pIdEmpresa = ?", params);
        print(result)
        return jsonify(username)
    else:
        return jsonify({'response' : 'no se obtuvo mensaje'})

if __name__ == '__main__':
    app.run()