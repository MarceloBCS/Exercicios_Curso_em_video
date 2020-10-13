from random import randint, seed

seed()

n = randint(0,999)

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'az':'\033[1;34m'}

if n%2 == 0:
    print('\nO nº gerado foi {0} e é {1}PAR{2}'.format(n, cor['amarelo'], cor['limp']))
else:
    print('\nO nº gerado foi {0} e é {1}ÍMPAR{2}'.format(n, cor['az'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))

