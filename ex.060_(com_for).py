from math import factorial

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'az':'\033[1;34m'}

x = 'C'
while x != 'S':
    n = int(input('Diga o nº para tirar o Fatorial: '))
    print(factorial(n))

    fatorial = 1
    for multiplicador in range(n,0,-1):
        fatorial = fatorial * multiplicador
        print(multiplicador, 'x ' if multiplicador > 1 else '= ', end='')

    print('{2}{0}! = {1}{3}'.format(n, fatorial, cor['amarelo'], cor['az']))
    print('-='*10)

    x = input(' digite [S] para sair do programa ou qualquer coisa para continuar → ').strip().upper()[0]
    print('-='*10, cor['limp'])

from datetime import date
print('\nProcessado em {}'.format(date.today()))