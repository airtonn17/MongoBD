from pymongo.mongo_client import MongoClient # Importando a biblioteca de conexão com o banco Mongo
import os # Importando biblioteca para usar recursos do SO (como acessar arquivos)
from dotenv import load_dotenv # Carregar as informações do arquivo .env (para proteger dados sensíveis)
import requests # Uma biblioteca que permite que me conecte com outras APIs
load_dotenv() # Carrega as variáveis do .env

"""
# # Criando a conexão com meu Banco de Dados
"""
# Acessa as variáveis de ambiente
uri = os.getenv("MONGO_URI")

# Exemplo de impressão dos dados .env
print("MONGO_URI:", uri)

# Create a new client and connect to the server
client = MongoClient(uri) # Preenchendo a variável client com o resultado da função MongoClient que cria a conexão com o MongoDB através dos dados contidos no parâmetro uri
db = client.teste # A variável db recebe a função que da nome (teste) ao meu BD
# db = MongoClient(uri).teste # Criando a conexão de forma mais compacta.

"""
# # Inserindo dados no Banco de Dados "teste" na coleção "test"
"""
# collection = db.test
# collection.insert_one({"nome":"Airton"})
# collection.insert_many([
#     {"nome": "João", "idade": 30, "cidade": "Rio de Janeiro"},
#     {"nome": "Ana", "idade": 22, "cidade": "Belo Horizonte"},
#     {"nome": "Carlos", "idade": 28, "cidade": "Curitiba"}
# ])

"""
# # Verificar se a conexão com o MongoDB foi estabelecida com sucesso
"""
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

"""
# # Buscando de forma manual um CEP e inserindo no meu Banco de Dados
"""
# cep = "70070600"  # CEP de exemplo
# url = f"https://viacep.com.br/ws/{cep}/json/" # Acesso à API que retorna os dados do CEP
#
# response = requests.get(url) # requests.get é uma função que busca (get) os dados do parametro url e aloca na variável response
# print(response.json())

# if response.status_code == 200:
#     data = response.json()
#     collection = db.endereco
#     collection.insert_one(data)
#     print(data)
# else:
#     print("Erro ao consultar o CEP")

"""
# # Exercício 1 - Transformar o código em uma Função
"""
# def buscacep(cepusuario):
#     url = f"https://viacep.com.br/ws/{cepusuario}/json/"
#     response = requests.get(url)
#     if cepusuario[5] != '-' :
#         substringinicial = cepusuario[:5]
#         substringfinal = cepusuario[5:]
#         cepusuario = substringinicial + '-' + substringfinal
#         print(cepusuario)
#
#     if response.status_code == 200:
#         data = response.json()
#         collection = db.endereco
#         documentos = list(collection.find({'cep':cepusuario}))
#         print(documentos)
#
#         if len(documentos) == 0:
#             documentos = collection.find({'bairro':'Coaçu'})
#             # collection.insert_one(data)
#         print("O resultado da sua busca é: \n", data)
#     else:
#         print("Erro ao consultar o CEP")
#
# print("-" * 30)
# print("    Bem Vindo ao Busca CEP")
# print("-" * 30)
# nome = input("Digite seu nome: ")
# cep = input(f"Olá, {nome}! Por favor digite seu CEP: ")
# buscacep(cep)
#
# while True:
#     continuar = input(f'{nome}, deseja pesquisar outro CEP? ')
#     continuar = continuar.lower()
#     if continuar == 'sim':
#         cep = input(f'Tudo bem {nome}, por favor digite outro CEP: ')
#         buscacep(cep)
#     else:
#         break
# print(f'Certo {nome}, obrigado por usar nossos serviços!')

"""
# # Exercício 2 - Remover informações repetidas do Banco de Dados
"""

def validacep(substring):
    if substring[5] != '-' :
        substringinicial = substring[:5]
        substringfinal = substring[5:]
        cepusuario = substringinicial + '-' + substringfinal
        print(cepusuario)
        return cepusuario

def buscacep(cepusuario):
    url = f"https://viacep.com.br/ws/{cepusuario}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        print("O resultado da sua busca é: \n", response.json())
        return response.json()
    else:
        print("Erro ao consultar o CEP")
        return

def salvarcep(cepdb, datacep):
    collection = db.endereco
    documentos = list(collection.find({'cep':cepdb}))
    print(documentos)

    if len(documentos) == 0:
        collection.insert_one(datacep)
        print(f"CEP {cepdb} salvo com sucesso!!",)
    else:
        print("CEP já consta no nosso banco")

def deletecep(cepdbdelete, datacepdelete):
    collection = db.endereco
    documentos = list(collection.find({'cep':cepdbdelete}))
    print(documentos)

    if len(documentos) != 0:
        print(f'Localizei estes dados através do CEP {cepdbdelete} ')
        confirmar = input(f'Tem certeza que deseja deletar o CEP {cepdbdelete}? Sim/Não ')
        confirmar = confirmar.lower()

        while confirmar != 'sim' or 'não':
            if confirmar == 'sim':
                collection.delete_one(datacepdelete)
                print(f"CEP {cepdbdelete} deletado com sucesso!",)
                break
            if confirmar == 'não':
                print(f'Entendi, o CEP {cepdbdelete} não foi apagado!')
                break
            else:
                print('Por favor, responda com "sim" ou "não".')
                confirmar = input(f'Tem certeza que deseja deletar o CEP {cepdbdelete}? Sim/Não ')
                confirmar = confirmar.lower()
    else:
        print(f"CEP {cepdbdelete} não encontrado no banco de dados.")

def continuar():
    while True:
        continuar = input(f'{nome}, deseja pesquisar outro CEP? ')
        continuar = continuar.lower()
        if continuar == 'sim':
            cep = input(f'Tudo bem {nome}, por favor digite outro CEP: ')
            resultbuscacep = buscacep(cep)
            resultvalidacep = validacep(cep)
            salvarcep(resultvalidacep, resultbuscacep)
        else:
            break
    print(f'Certo {nome}, obrigado por usar nossos serviços!')


# Main
print("-" * 31)
print("      API Gerencía CEP")
print("-" * 31)
nome = input("Porfavor, digite seu nome: ")
print(f'Bem vindo(a) {nome}!')
opcao = input('Digite o numero que corresponde ao serviço deseja fazer: ')
print('Buscar um CEP: [1]')
print('Deletar um CEP: [2]')
if opcao == 1:

cep = input(f"Olá, {nome}! Por favor digite seu CEP: ")


resultbuscacep = buscacep(cep)
resultvalidacep = validacep(cep)
# salvarcep(resultvalidacep, resultbuscacep)
deletecep(resultvalidacep, resultbuscacep)
continuar()
