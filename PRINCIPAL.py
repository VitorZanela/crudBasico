def menu():
    global usuarios
    print  ('[1] Adicionar novo contato\n'
        '[2] Ver contatos\n'
        '[0] Sair')
    primeiraEscolha = int(input('Digite a opção1: '))
    if primeiraEscolha == 1:
        adicionarContato()
    elif primeiraEscolha == 2:
        if len(usuarios) == 0:
            print('Não há contatos cadastrados! Tente novamente')
            menu()
        else:
            verContato()
    elif primeiraEscolha == 0:
        print('Programa Encerrado! Volte Sempre.')


def adicionarContato():
    global cadastro
    global usuarios
    cadastro['Nome'] = str(input("Nome: "))
    cadastro['Telefone'] = int(input("Telefone: "))
    cadastro['Email'] = str(input('Email: '))
    usuarios.append(cadastro.copy())
    print('USUARIO CADASTRADO COM SUCESSO!!')
    menu()


def verContato():
    global cadastro
    global usuarios
    for p in cadastro.keys():
        print(f'{p:<15}', end='')
    print()
    for chave, valores in enumerate(usuarios):
        for v in valores.values():
            print(f'{str(v):<14}', end=' ')
        print()
    while True:
        print('[1] Adicionar novo contato\n'
            '[2] Atualizar contato\n'
            '[3] Remover contato\n'
            '[0] Sair')
        msg = int(input('Digite a opção: '))
        if msg == 1:
            adicionarContato()
        elif msg == 2:
            atualizarContato()
        elif msg == 3:
            print()#removerContato()
        elif msg == 0:
            print('Programa Encerrado! Volte Sempre.')
            break

def atualizarContato():
    global cadastro
    global usuarios
    print('cod ', end=' ')
    for p in cadastro.keys():
        print(f'{p:<15}', end='')
    print()
    for chave, valores in enumerate(usuarios):
        print(f'{chave:<5}', end='')
    for v in valores.values():
        print(f'{str(v):<15}', end='')
    print()
    while True:
        escolha = int(input('Qual contato deseja atualizar? (999 para cancelar): '))
        if escolha == 999:
            break
        elif escolha >= len(usuarios):
            print('ERRO! Opção invalida')
        else:
            print(f' -> ALTERANDO DADOS DE USUÁRIO: {usuarios[escolha]["Nome"]}')




cadastro = {}
usuarios = []

#Menu interativo
menu()

    

print(cadastro)
print(usuarios)

