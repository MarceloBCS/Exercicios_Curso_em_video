n = input('diga o seu nome completo: ').strip()

cor = {'az':'\033[1;34m', 'limp':'\033[m'}

print(n.upper())
print(n.lower())

l = len(n)
e = n.count(' ')
print('letras ----->', l)
print('\nseu nome tem ao todo: {1}{0} letras{2}'.format((l-e), cor['az'], cor['limp']))
print('\n', type(n), type(l), type(e))

nome = n.split(' ')
print('\n', n.split(' '))
print('\no {2}1º nome tem {0} letras{3} e o {2}último nome tem {1} letras{3}'
      .format(len(nome[0]), len(nome[-1]), cor['az'], cor['limp']))

import datetime

print('\nProcessado em {}'.format(datetime.date.today().today()))







