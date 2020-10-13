n = float(input('escreva o nº: '))
from math import trunc, ceil, floor, sqrt

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

print('\no nº {0} tem a parte inteira = {2}{1}{3}'.format(n, trunc(n), cor['amarelo'], cor['limp']))
print('\na raiz quadrada de {0} é: {4}{1:.2f}{5},\narredondando para baixo é: {4}{2}{5}\narredondando para cima é: {4}{3}{5}'
      .format(n, sqrt(n), floor(sqrt(n)), ceil(sqrt(n)), cor['amarelo'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))






