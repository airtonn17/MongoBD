from pymongo.mongo_client import MongoClient

import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Acessa as variáveis de ambiente
uri = os.getenv("MONGO_URI")

# Exemplo de impressão
print("MONGO_URI:", uri)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.teste
collection = db.test
collection.insert_one({"nome":"Airton"})
collection.insert_many([
    {"nome": "João", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Ana", "idade": 22, "cidade": "Belo Horizonte"},
    {"nome": "Carlos", "idade": 28, "cidade": "Curitiba"}
])
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

