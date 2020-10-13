r1 = float(input('\nDiga o comprimento da reta1: '))
r2 = float(input('diga o comprimento da reta2: '))
r3 = float(input('diga o comprimento da reta3: '))

cor = {'red':'\033[1;31m', 'az':'\033[1;34m', 'amarelo':'\033[1;33m', 'verde':'\033[1;32m', 'limp':'\033[m'}

s = [r1, r2, r3]
maior = max(s)
menor = min(s)

soma = r1 + r2 + r3
medio = soma - maior - menor

if (medio + menor) > maior:
    print('\npode formar um triângulo')
    if r1 == r2 == r3:
        print('\nO triângulo com todos os lados iguais a {0} é {1}equilátero{2}'.format(r1, cor['verde'], cor['limp']))
    elif medio == maior or medio == menor: #and menor != maior:
        print('\nO triângulo com lados {0}, {1} e {2} é {3}isósceles{4}'.format(menor, medio, maior, cor['amarelo'], cor['limp']))
    else:
        print('\nO triangulo com 3 lados diferentes {0}, {1} e {2} é {3}escaleno{4}'.format(r1, r2, r3, cor['az'], cor['limp']))
else:
    print('\n', cor['red'], 'NÃO PODE formar um triângulo', cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today()))