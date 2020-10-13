c_oposto = float(input('\ndiga o cateto oposto: '))
c_adjacente = float(input('diga o cateto adjacente '))

import math

cor = {'red':'\033[1;31m','limp':'\033[m', 'az':'\033[1;34m'}

hip = ((c_oposto**2) + (c_adjacente**2))**(0.5)

print('\nhipotenusa = ', cor['red'], hip, cor['limp'])
print('hiponetusa = ', cor['az'], math.hypot(c_oposto, c_adjacente), cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
