l = float(input('\nYoung Grasshopper, diga a largura [m2]: '))
h = float(input('diga a altura [m2]: '))
area = l * h
tinta = area / 2

cor = {'amarelo':'\033[1;33m', 'verm':'\033[1;31m', 'limp':'\033[m'}

print('\nvc precisará de {2}{0:^5.1f} litros{4} para pintar uma área de {3}{1:^5.2f} m2{4}'
      .format(tinta, area, cor['amarelo'], cor['verm'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))



