cor = ('\033[m',        # 0 - limpeza
       '\033[1;31m',    # 1 - vermelho
       '\033[1;33m',    # 2 - amarelo
       '\033[1;34m',    # 3 - azul
       '\033[1;36m',    # 4 - verde claro
       '\033[1;30;44m'  # 5 - azul com fundo
       )

def linha(simbolo):
    print(simbolo*40)


def cabeçalho(txt):
    linha('-')
    print(cor[5], txt.center(38), cor[0])
    linha('-')


def menu(lista):
    c = 1
    for itens in lista:
        print('{2}{0}{4} - {3}{1}{4}'.format(c, itens, cor[2], cor[3], cor[0]))
        c += 1
    linha('-')


def escolha(txt):
    print(cor[4], end='')
    opcao = input(txt)                  #Input para o usuário escolher uma das opções
    print(cor[0], end='')
    return opcao


def leia_int(txt):
    while True:
        opcao = escolha('*** Sua opção: ')
        try:
            opcao = int(opcao)          # testa a opção do usuário. Se for um nº inteiro, retorna via "else"
        except:
            errado(txt)                 # Chama a função para erros de escolha no menu pelo usuário
        else:
            return opcao


def errado(txt):
    print(cor[1], txt, cor[0])
    print('-' * 40)


