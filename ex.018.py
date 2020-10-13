n = float(input('\nYoung Grasshopper, diga um angulo qualquer em [graus] '))

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

import math

r = math.radians(n)

sen = math.sin(r)
cos = math.cos(r)
tan = math.tan(r)

print('\nsen {0}º = {4}{1:.2f}{5}\ncos {0}º = {4}{2:.2f}{5}\ntag {0}º = {4}{3:.2f}{5}'.format(n, sen, cos, tan, cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


