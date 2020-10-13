a1: str = input('nome do 1º aluno: ')
a2 = input('nome do 2º aluno: ')
a3 = input('nome do 3º aluno: ')
a4 = input('nome do 4º aluno: ')

cor = {'red':'\033[31m', 'limp':'\033[m', 'az':'\033[1;34m', 'amarelo':'\033[1;33m'}

lista = [a1, a2, a3, a4]

from random import shuffle, choice

shuffle(lista)
print('\nshuffle: ', cor['red'], lista, cor['limp'])
print('\na lista está:', cor['amarelo'], lista, cor['limp'])
print('\nchoice: ', cor['az'], choice(lista), cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


