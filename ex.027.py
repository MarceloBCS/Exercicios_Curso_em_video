nome = input('diga o seu nome completo ').strip()

n = nome.split(' ')

cor = {'yellow':'\033[1;33m', 'limp':'\033[m'}

print('\nprimeiro nome: {2}{0}{3} \n último nome é {2}{1}{3} '.format(n[0], n[-1], cor['yellow'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))



