from modulos.layout import *
from time import sleep
import json

def verificarArquivo(arq):
    try:
        with open(arq, 'r') as f:
            json.load(f)
        return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False

def criarArquivo(arq):
    try:
        with open(arq, 'w') as f:
            json.dump([], f)
    except:
        cabecalho('Erro ao criar Arquivo')

def lerContatos(arq):
        try:
            with open(arq, 'r') as f:
                contatos = json.load(f)
        except:
            cabecalho('Erro ao ler arquivo')
        else:
            for contato in contatos:
                print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}")


def adicionarCont(arq,nome,tel,email):
    try:
        with open(arq, 'r') as f:
            contatos = json.load(f)
        contatos.append({"nome": nome, "telefone": tel, "email": email})
        with open(arq, 'w') as f:
            json.dump(contatos, f, indent=4)
    except:
        cabecalho('Erro ao cadastrar')
    else:
        cabecalho(f'{nome} cadastrado com sucesso!')

def excluirContatos(arq):
    try:
        with open(arq, 'r') as f:
            a = json.load(f)
    except:
        cabecalho('Erro ao ler arquivo!')
    else:
        while True:
            sleep(1)
            for chave, pessoa in enumerate(a):
                print(f'{chave+1} - {pessoa["nome"]}')
            print('0 - Cancelar exclusão')
            linha()
            opc = leiaInt('Digite a opção de exclusão: ')
            if opc >= 1 and opc < len(a)+1:
                del a[opc - 1]
                with open(arq, 'w') as f:
                    json.dump(a, f, indent=4)
                cabecalho(f'Contato excluido com sucesso')
                break
            elif opc == 0:
                break
            else:
                cabecalho('Opção Invalida! Tente novamente.')

def atualizarContato(arq):
    try:
        with open(arq, 'r') as f:
            contatos = json.load(f)
    except:
        cabecalho('Erro ao ler arquivo')
        return

    while True:
        for i, contato in enumerate(contatos):
            print(f'{i+1} - {contato["nome"]}')
        print('0 - Cancelar alteração')
        linha()
        opcao = leiaInt('Digite qual contato quer alterar: ')
        sleep(1)

        if opcao >= 1 and opcao <= len(contatos):
            contato = contatos[opcao - 1]
            campos = list(contato.keys())
            print('\nDados do contato:')
            for i, campo in enumerate(campos):
                print(f'{i+1} - {campo.capitalize()}: {contato[campo]}')
            print('0 - Cancelar alteração')
            linha()
            campo = leiaInt('Qual campo deseja alterar? ')

            if campo >= 1 and campo <= len(campos):
                novo = input('Digite o novo dado: ')
                contatos[opcao - 1][campos[campo - 1]] = novo
                with open(arq, 'w') as f:
                    json.dump(contatos, f, indent=4)
                cabecalho('Contato atualizado com sucesso!')
                break
            elif campo == 0:
                break
            else:
                cabecalho('Campo inválido! Tente novamente.')
                break

        elif opcao == 0:
            break
        else:
            cabecalho('Opção inválida! Tente novamente.')