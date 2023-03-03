# Desenvolvido por Kairo Trzeciak
# https://github.com/kairodev
import os
from flask import Flask, request
from functions import *

app = Flask(__name__)

# ROTA - Visualização dos dados
@app.route('/data')
def data():
    return viewData()

# ROTA - Visualização de dados de um usuário especifico
@app.route('/specific/data/<id>')
def dataSpecific(id):
    return viewDataSpecific(id)

# ROTA - Resetar DB
@app.route('/reset', methods=['DELETE'])
def reset():
    return resetDatabase()

# ROTA - Deletar usuário
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    return deleteUser(id)

# ROTA - Alterar usuário
@app.route('/change/<id>', methods=['POST'])
def change(id):
    username = request.form.get('username')
    password = request.form.get('password')
    return changeUser(id, username, password)

if __name__ == '__main__':

    createData()
    while createData():
        try:
            app.run(debug=True) 
        except Exception as e:
            print(e)
            continue
