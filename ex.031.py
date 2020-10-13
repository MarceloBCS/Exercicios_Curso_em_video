d = float(input('Qual é a distância da sua viagem em Km? '))

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

if d <= 200:
    p = 0.50 * d
    print('\nVc vai pagar R${0:.2f} para rodar {2}{1:.1f} km{3}'.format(p, d, cor['amarelo'], cor['limp']))
else:
    p = 0.45 * d
    print('\nVc vai pagar R${0:.2f} para rodar {2}{1:.1f} km{3}'.format(p, d, cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
