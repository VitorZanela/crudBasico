def menu():
    print  ('[1] Adicionar contato\n'
            '[2] Ver contatos\n'
            '[3] Atualizar contato\n'
            '[4] Remover contato\n'
            '[0] Sair')
    while True:
        msg = int(input('Digite a opção: '))
        if msg == 1:
            adicionar()
        if msg == 2:
            vercontato()
        elif msg == 0:
            break

def adicionar():
    global cadastro
    global usuarios
    cadastro['Nome'] = str(input("Nome: "))
    cadastro['Telefone'] = int(input("Telefone: "))
    cadastro['Email'] = str(input('Email: '))
    usuarios.append(cadastro.copy())

    return cadastro

def vercontato():
    global cadastro
    global usuarios
    print('Cod', end=' ')
    for p in cadastro.keys():
        print(f'{p:<15}', end='')
    print()
    for chave, v in enumerate(usuarios):
        print(f'{chave:<3}', end='')
        for valores in cadastro.values():
            print(f'{str(valores):<15}', end=' ')
        print()



cadastro = {}
usuarios = []

#Menu interativo
menu()




