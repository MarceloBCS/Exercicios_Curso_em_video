r1 = float(input('\ndiga o comprimento do 1º lado: '))
r2 = float(input('diga o comprimento do 2º lado: '))
r3 = float(input('diga o comprimento do 3º lado: '))

cor = {'red':'\033[1;31m', 'verde':'\033[1;32m', 'limp':'\033[m', 'az':'\033[1;34m', 'amarelo':'\033[1;33m'}

s = [r1, r2, r3]
s_ord = sorted(s)

menor = s_ord[-3]
med = s_ord[-2]
maior = s_ord[-1]

if (menor + med) > maior:
    print('\nEstes 3 lados podem formar um triângulo')
    if menor == med == maior:
        print('\nEste triangulo com 3 lados iguais a {0} é {1}Equilátero{2}'.format(r1, cor['verde'], cor['limp']))
    elif menor == med or med == maior:
        print('\nEste triangulos com lados {0}, {1} e {2} é {3}isósceles{4}'.format(menor, med, maior, cor['amarelo'], cor['limp']))
    else:
        print('\nO triangulo formado com 3 lados diferentes {}, {} e {} é {}escaleno{}'.format(menor, med, maior, cor['az'], cor['limp']))
else:
    print('\nCom estas 3 retas, {}não é possível formar um triângulo{}'.format(cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today()))