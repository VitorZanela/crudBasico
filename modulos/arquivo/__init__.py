from modulos.layout import *

def verificarArquivo(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        cabecalho('Erro ao criar Arquivo')

def lerContatos(arq):
    try:
        a = open(arq, 'rt')
    except:
        cabecalho('Erro ao ler arquivo')
    else: 
        for pessoa in a:
            dado = pessoa.split(';')
            dado[2] = dado[2].replace('\n','')
            print(f'Nome: {dado[0]} - Telefone: {dado[1]} -  E-mail: {dado[2]}')
    finally:
        a.close()

def adicionarCont(arq,nome,tel,email):
    try:
        a = open(arq, 'at')
    except:
        cabecalho('Erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{tel};{email}\n')
        except:
            cabecalho('Não foi possivel cadastrar')
        else:
            cabecalho(f'{nome} cadastrado com sucesso!')
    finally:
        a.close()

def excluirContatos(arq):
    try:
        with open(arq, 'r') as f:
            a = f.readlines()
    except:
        cabecalho('Erro ao ler arquivo!')
    else:
        while True:
            sleep(1)
            for chave, pessoa in enumerate(a):
                dado = pessoa.strip().split(';')
                print(f'{chave+1} - {dado[0]}')
            print('0 - Cancelar exclusão')
            linha()
            opc = leiaInt('Digite a opção de exclusão: ')
            if opc >= 1 and opc < len(a)+1:
                del a[opc - 1]
                b = open(arq, 'w')
                b.writelines(a)
                b.close()
                cabecalho(f'Contato excluido com sucesso')
                break
            elif opc == 0:
                break
            else:
                cabecalho('Opção Invalida! Tente novamente.')

def atualizarContato(arq):
    try:
        with open(arq, 'r') as f:
            a = f.readlines()
    except:
        cabecalho('Erro ao ler arquivo')
        return
    while True:
        for i, pessoa in enumerate(a):
            dado = pessoa.strip().split(';')
            print(f'{i+1} {dado[0]}')
        print('0 - Cancelar alteração')
        linha()
        opção = leiaInt('Digite qual contato quer alterar: ')
        sleep(1)
        if opção >= 1 and opção <= len(a):
            dado = a[opção - 1].strip().split(';')
            print('\nDados do contato:')
            for i, campo in enumerate(dado):
                print(f'{i+1} - {campo}')
            print('0 - Cancelar alteração')
            linha()
            campo = leiaInt('Qual campo deseja alterar? ')
            while True:
                if campo >= 1 and campo <= len(dado):
                    novo = input(f'Digite o novo dado: ')
                    dado[campo - 1] = novo
                    a[opção - 1] = ';'.join(dado) + '\n'
                    b = open(arq, 'w')
                    b.writelines(a)
                    b.close()
                    cabecalho('Contato atualizado com sucesso!')
                    break
                elif campo == 0:
                    break
                else:
                    cabecalho('Campo invalido! Tente novamente.')
                    break
            break
        elif opção == 0:
            break
        else:
            cabecalho('Opção invalida! Tente novamente.')