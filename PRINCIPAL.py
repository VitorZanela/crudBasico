from modulos.layout import *
from modulos.arquivo import *

arq = 'contatos.json'

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
        while True:
            opc = menuContatos(['Adicionar Novo Contato', 'Atualizar Contato', 'Excluir Contato','Ver Contatos Atualizados','Sair'])
            if opc == 1:
                cabecalho('ADICIONANDO NOVO CONTATO')
                nome = str(input('Nome: '))
                tel = int(input('Telefone: '))
                email = str(input('Email: '))
                adicionarCont(arq, nome, tel, email)
                cabecalho('CONTATOS ATUALIZADOS')
                lerContatos(arq)
            elif opc == 2:
                cabecalho('ESCOLHA O CONTATO')
                atualizarContato(arq)
            elif opc == 3:
                cabecalho('ESCOLHA O CONTATO')
                excluirContatos(arq)
            elif opc == 4:
                cabecalho('CONTATOS ATUALIZADOS')
                lerContatos(arq)
            elif opc == 5:
                cabecalho('Programa Encerrado. Até logo!')
                break
            else:
                cabecalho('Opção Invalida, Tente novamente!')
        break
    elif escolha == 3:
        cabecalho('Programa Encerrado. Até logo!')
        break
    else:
        cabecalho('Opção invalida! Tente novamente.')

