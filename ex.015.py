km = float(input('Qual a KM que vc percorreu? '))
d = int(input('Quantos dias o carro foi alugado? '))

pagar = 0.15*km + 60*d

cor = {'verm':'\033[1;31m', 'limp':'\033[m'}

print('\nRodando {0:>10.2f} km\n em {1:>10.1f} dias,\n gera uma {3}fatura de R$ {2:<10.2f}{4}'
      .format(km, d, pagar, cor['verm'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


