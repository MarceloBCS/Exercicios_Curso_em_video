ano = int(input('Qual o ano que vc gostaria de saber se é bissexto (Use ZERO para saber o ano atual)? '))

cor = {'red':'\033[1;31m', 'az':'\033[1;34m', 'limp':'\033[m'}

import datetime

if ano == 0:
    ano = datetime.date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 and ano % 100 == 0):
    print('\nO ano {0} {1}é ano bissexto{2}'.format(ano, cor['az'], cor['limp']))
else:
    print('\no ano {0} {1}NÃO é{2} bissexto'.format(ano, cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
