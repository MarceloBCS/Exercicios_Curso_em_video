cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

n = int(input('\ndiga quantos termos da sequência de Fibonacci: '))
a = 0
b = 1
c = 1
contador = 3
print(cor['amarelo'], a, cor['limp'], end=' → ')
print(cor['amarelo'], b, cor['limp'], end=' → ')
print(cor['amarelo'], c, cor['limp'], end=' → ')

while contador < n:
    a = b + c
    b = c
    c = a
    contador += 1
    print(cor['amarelo'], a, cor['limp'], ' → ' if contador < n else '\033[1;31m  FIM  \033[m', end='')

from datetime import date
print('\n\nProcessado em {}'.format(date.today()))