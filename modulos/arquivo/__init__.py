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
