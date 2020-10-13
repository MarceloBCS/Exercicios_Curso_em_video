cor = {'am':'\033[1;33;40m', 'red':'\033[1;31;40m', 'az':'\033[1;30;44m', 'rx':'\033[1;35;40m', 'ver':'\033[7;32;40m',
       'enfase':'\033[1;30;45m', 'lim':'\033[m'}


def cabe_help(txt):
    c = len(txt)
    print(cor['ver'], '~'*c)
    print(txt)
    print('', '~'*c)
    print(cor['lim'], end='')


def comando(txt):
    c = len('  Acessando o manual do comando   ' + txt)
    print(cor['az'], '~'*c)
    print(f'  Acessando o manual do comando \'{txt}\' ')
    print('', '~'*c)


fim = ''
while True:
    cabe_help('  Sistema de Ajuda PyHELP')
    fim = input('Função/Biblioteca ou [fim para sair] > ').strip().lower()
    if fim != 'fim':
        comando(fim)
        print(cor['enfase'])
        help(fim)
        print(cor['lim'])
    else:
        break

from datetime import date
print(f'\nProcessado em {date.today()}')
