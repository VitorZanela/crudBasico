from time import sleep


def menu():
    while True:
        global usuarios
        sleep(1)
        print(f'-'*40)
        print('MENU PRINCIPAL'.center(40))
        print('-'*40)
        print  ('\033[1;33m1\033[m - \033[1;34mAdicionar novo contato\033[m\n'
            '\033[1;33m2\033[m - \033[1;34mVer contatos\033[m\n'
            '\033[1;33m3\033[m - \033[1;34mSair\033[m')
        print('-'*40)
        escolha = int(input('\033[0;33mSua Opção:\033[m '))
        if escolha == 1:
            adicionarContato()
            break
        elif escolha == 2:
            if len(usuarios) == 0:
                print('-'*40)
                print('\033[0;31mNão há contatos cadastrados! Tente novamente\033[m')
                menu()
                break
            else:
                verContato()
                break
        elif escolha == 3:
            print('-'*40)
            print('Programa Encerrado! Volte Sempre.')
            print('-'*40)
            break


def adicionarContato():
    global cadastro
    global usuarios
    print(f'-'*40)
    print('CADASTRO DE USUARIO'.center(40))
    print('-'*40)
    cadastro['Nome'] = str(input("Nome:     "))
    cadastro['Telefone'] = int(input("Telefone: "))
    cadastro['Email'] = str(input('Email:    '))
    usuarios.append(cadastro.copy())
    print('-'*40)
    print('\033[1;32mUSUARIO CADASTRADO COM SUCESSO!!\033[m')
    menu()


def verContato():
    global cadastro
    global usuarios
    print(f'-'*40)
    print('USUARIOS'.center(40))
    print('-'*40)
    for p in cadastro.keys():
        print(f'\033[4m{p:<15}\033[0m', end='')
    print()
    for chave, valores in enumerate(usuarios):
        for v in valores.values():
            print(f'{str(v):<14}', end=' ')
        print()
    print('-'*40)
    while True:
        print  ('\033[1;33m1\033[m - \033[1;34mAdicionar novo contato\033[m\n'
        '\033[1;33m2\033[m - \033[1;34mAtualizar contato\033[m\n'
        '\033[1;33m3\033[m - \033[1;34mRemover contato\033[m\n'
        '\033[1;33m0\033[m - \033[1;34mSair\033[m')
        print('-'*40)
        msg = int(input('\033[0;33mSua Opção:\033[m '))
        if msg == 1:
            adicionarContato()
            break
        elif msg == 2:
            atualizarContato()
            break
        elif msg == 3:
            print()#removerContato()
            break
        elif msg == 0:
            print('-'*40)
            print('Programa Encerrado! Volte Sempre.')
            print('-'*40)
            break
        else:
            print('\033[0;31mOpção Invalida\033[m')
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

