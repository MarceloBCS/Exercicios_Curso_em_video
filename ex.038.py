n1 = int(input('diga o 1º número inteiro: '))
n2 = int(input('diga o 2º número inteiro: '))

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

if n1 > n2:
    print(cor ['red'], '\no 1º valor é maior', cor['limp'])
elif n1<n2:
    print(cor['red'], '\no 2º valor é maior', cor['limp'])
else:
    print(cor['red'], '\nNão existe valor maior. Ambos são iguais', cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))