# from pymongo.mongo_client import MongoClient
# import os
# from dotenv import load_dotenv
# # Carrega as variáveis do .env
# load_dotenv()

# # Acessa as variáveis de ambiente
# uri = os.getenv("MONGO_URI")
#
# # Exemplo de impressão
# print("MONGO_URI:", uri)

# Create a new client and connect to the server
#
# client = MongoClient(uri)
# db = client.teste

# collection = db.endereco
# collection.insert_one({'cep': '60871-640', 'logradouro': 'Rua José Cavalcante Sobrinho', 'complemento': '', 'unidade': '', 'bairro': 'Coaçu', 'localidade': 'Fortaleza', 'uf': 'CE', 'estado': 'Ceará', 'regiao': 'Nordeste', 'ibge': '2304400', 'gia': '', 'ddd': '85', 'siafi': '1389'})

# collection = db.test
# collection.insert_one({"nome":"Airton"})
# collection.insert_many([
#     {"nome": "João", "idade": 30, "cidade": "Rio de Janeiro"},
#     {"nome": "Ana", "idade": 22, "cidade": "Belo Horizonte"},
#     {"nome": "Carlos", "idade": 28, "cidade": "Curitiba"}
# ])
# Send a ping to confirm a successful connection


# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from pymongo.mongo_client import MongoClient # Importando a biblioteca de conexão com o banco Mongo
import os # Importando biblioteca para usar recursos do SO (como acessar arquivos)
from dotenv import load_dotenv # Carregar as informações do arquivo .env (para proteger dados sensíveis)
import requests # Uma biblioteca que permite que me conecte com outras APIs
load_dotenv() # Carrega as variáveis do .env

# Acessa as variáveis de ambiente
uri = os.getenv("MONGO_URI") # Acessando os dados da variável de ambiente

# Exemplo de impressão dos dados .env
print("MONGO_URI:", uri)

client = MongoClient(uri) # Preenchendo a variável client com o resultado da função MongoClient que cria a conexão com o MongoDB através dos dados contidos no parâmetro uri
db = client.teste # A variável db recebe a função que da nome ao meu BD

cep = "70070600"  # CEP de exemplo
url = f"https://viacep.com.br/ws/{cep}/json/" # Acesso à API que retorna os dados do CEP

response = requests.get(url) # requests.get é uma função que busca (get) os dados do parametro url e aloca na variável response
print(response.json())

if response.status_code == 200:
    data = response.json()
    collection = db.endereco
    collection.insert_one(data)
    print(data)
else:
    print("Erro ao consultar o CEP")