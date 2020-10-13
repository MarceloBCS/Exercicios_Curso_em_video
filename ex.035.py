r1 = float(input('\ninforme o comprimento da 1º reta '))
r2 = float(input('informe o comprimento da 2º reta '))
r3 = float(input('informe o comprimento da 3º reta '))

cor = {'red':'\033[1;31m', 'limp':'\033[m', 'az':'\033[1;34m'}

#desigualdade triangular: para formar um triangulo, os 2 lados menores somados tem que OBRIGATORIAMENTE ser maior que o lado maior

t = [r1, r2, r3]

menor = min(t)
maior = max(t)

soma = r1 + r2 + r3
mediano = soma - menor - maior

if (menor + mediano) > maior:
    print('\n{3}Pode formar um triângulo{4} {0:.1f}, {1:.1f} e {2:.1f}'.format(menor, mediano, maior, cor['az'], cor['limp']))
else:
    print('\nEstas retas {0:.1f}, {1:.1f} e {2:.1f} {3}NÃO podem{4} formar um triângulo'.format(menor, mediano, maior, cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
