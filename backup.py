if len(documentos) != 0:
    print(f'Localizei estes dados através do CEP {cepdbdelete} ')
    confirmar = input(f'Tem certeza que deseja deletar o CEP {cepdbdelete}? Sim/Não ')
    confirmar = confirmar.lower()

    while confirmar != 'sim' or 'não':
        if confirmar == 'sim':
            collection.delete_one(datacepdelete)
            print(f"CEP {cepdbdelete} deletado com sucesso!", )
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