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
        a = open(arq, 'r')
    except:
        print('Erro ao ler arquivo')
    else: 
        for i, pessoa in enumerate(a):
            dado = pessoa.split(';')
            dado[2] = dado[2].replace('\n','')
            print(f'{i+1} {dado[0]}')
        linha()
        opção = leiaInt('Digite a opção de Exclusão: ')
        if opção >= 0 and opção < len(dado):
            del dado[opção]
            b = open(arq, 'w') #ta excluindo todos os contatos
            b.writelines(a)
            b.close()
        else:
            print('Opção invalida')

    finally:
        a.close()