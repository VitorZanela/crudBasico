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
        print('Erro ao criar Arquivo')

def lerContatos(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler arquivo')
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
        print('Erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{tel};{email}\n')
        except:
            print('Não foi possivel cadastrar')
        else:
            print(f'{nome} cadastrado com sucesso!')
    finally:
        a.close()

def excluirContatos(arq):
    try:
        with open(arq, 'r') as f:
            a = f.readlines()
    except:
        print('Erro ao ler arquivo')
    else: 
        for i, pessoa in enumerate(a):
            dado = pessoa.strip().split(';')
            print(f'{i+1} {dado[0]}')
        linha()
        opção = leiaInt('Digite a opção de Exclusão: ')
        if opção >= 0 and opção < len(a)+1:
            del a[opção-1]
            b = open(arq, 'w')
            b.writelines(a)
            b.close()
        else:
            print('Opção invalida')

def atualizarContato(arq):
    try:
        with open(arq, 'r') as f:
            a = f.readlines()
    except:
        print('Erro ao ler arquivo')
        return
    for i, pessoa in enumerate(a):
        dado = pessoa.strip().split(';')
        print(f'{i+1} {dado[0]}')
    linha()
    opção = leiaInt('Digite qual dado quer alterar: ')
    if opção >= 1 and opção <= len(a):
        dado = a[opção - 1].strip().split(';')
        print('\nDados do contato:')
        for i, campo in enumerate(dado):
            print(f'{i+1} - {campo}') 
        linha()
        campo = leiaInt('Qual campo deseja alterar? ')
        if campo >= 1 and campo <= len(dado):
            novo = input('Digite o novo valor: ')
            dado[campo - 1] = novo
            a[opção - 1] = ';'.join(dado) + '\n'
            b = open(arq, 'w')
            b.writelines(a)
            b.close()
            print('Contato atualizado com sucesso!')
        else:
            print('Campo invalido')
    else:
        print('Opção invalida')