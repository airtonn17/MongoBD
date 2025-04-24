from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import os
from service import buscacepservice, validacepservice

load_dotenv()

uri = os.getenv("MONGO_URI")
db = MongoClient(uri).teste

app = Flask(__name__)
CORS(app)  # Libera todas as origens


@app.route('/api/buscacep', methods=['GET'])
def buscacep():
    cepusuario = request.args.get('cep')
    return buscacepservice(cepusuario)

@app.route('/api/editacep/<string:numerocep>', methods=['PUT'])
def editacep(numerocep):
    collection = db.endereco
    edita_bairro = request.get_json().get('bairro')
    edita_logradouro = request.get_json().get('logradouro')
    # documentos = list(collection.find({'cep': numerocep}))
    print(numerocep)
    cep_validado = validacepservice(numerocep)
    filtro = {'cep': cep_validado}
    novos_valores = {'$set': {'logradouro': edita_logradouro, 'bairro':edita_bairro}}
    docatualizado = collection.update_many(filtro, novos_valores)
    return 'ok'


@app.route('/api/salvarcep', methods=['POST'])
def salvarcep():
    salvacep1 = request.get_json().get('cep1')
    databusca = buscacepservice(salvacep1)
    print(salvacep1)
    collection = db.endereco
    print(collection)
    documentos = list(collection.find({'cep':salvacep1}))
    print(documentos)


    if len(documentos) == 0:
        collection.insert_one(databusca)
        return f"CEP {salvacep1} salvo com sucesso!!"
    else:
        return "CEP já consta no nosso banco"


@app.route('/api/deletecep/<string:numerocep>', methods=['DELETE'])

def deletecep(numerocep):
    collection = db.endereco
    cep_validado = validacepservice(numerocep)
    collection.delete_one({"cep": cep_validado})
    return f"CEP {cep_validado} deletado com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)