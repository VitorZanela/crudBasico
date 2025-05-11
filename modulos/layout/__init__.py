from time import sleep

def linha(tam=40):
    print('-'*tam)

def cabecalho(txt):
    linha()
    print(F'   \033[1m{txt}\033[m'.center(40))
    linha()

def menu(lista):
    while True:
        sleep(1)
        cabecalho('MENU PRINCIPAL')
        for chave, valor in enumerate(lista):
            print(f'{chave+1} - {valor}')
        linha()
        opc = leiaInt('Sua Opção: ')
        return opc
    
def leiaInt(txt):
    try:
        n = int(input(txt))
    except:
        print('ERRO! Opção Invalida!')
    else:
        return n