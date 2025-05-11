from modulos.layout import *
from modulos.arquivo import *

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




arq = 'contatos.txt'

if not verificarArquivo(arq):
    criarArquivo(arq)

#Menu interativo
while True:
    escolha = menu(['Adicionar Novo Contato','Ver Contatos','Sair'])
    if escolha == 1:
        cabecalho('ADICIONANDO NOVO CONTATO')
        nome = str(input('Nome: '))
        tel = int(input('Telefone: '))
        email = str(input('Email: '))
        adicionarCont(arq, nome, tel, email)
    elif escolha == 2:
        cabecalho('CONTATOS ADICIONADOS')
        lerContatos(arq)
    elif escolha == 3:
        cabecalho('Programa Encerrado. Até logo!')
        break

