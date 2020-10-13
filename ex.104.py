cor = {'red':'\033[1;31m', 'limp':'\033[m', 'evidencia':'\033[1;30;47m'}


def leiaint(txt):
    n = input(txt)
    while not n.isdigit():
        print(cor['red'], 'ERRO! Digite um número inteiro válido', cor['limp'])
        print('-'*(len('Erro! Digite um número inteiro válido')+1))
        n = input(txt)
    return n


n = leiaint('Digite um número: ')
print('Vc acabou de digitar o {1} número {0} {2}'.format(n, cor['evidencia'], cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')