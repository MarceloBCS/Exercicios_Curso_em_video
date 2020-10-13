cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

a = int(input('\ndiga o 1º termo da PA: '))
r = int(input('diga a razão da PA: '))
n = int(input('diga quantos termos nesta PA: '))
print('-='*12)

contador = 1

while contador < n+1:
    print(cor['amarelo'], a, cor['limp'], end=' → ')
    a = a + r
    contador += 1

from datetime import date
print('\n\nProcessado em {}'.format(date.today()))

