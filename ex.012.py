n = float(input('\nYoung Grasshopper, diga o preço corrente: R$ '))
p = n * 0.95

cor = {'verm':'\033[1;31;40m', 'az':'\033[1;34;40m', 'limp':'\033[m'}

print('\nna {2}Promoção{4}, ao invés de pagar R${0:^5.2f}, vc vai pagar APENAS {3}R${1:^5.2f}{4}'
      .format(n, p, cor['az'], cor['verm'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


