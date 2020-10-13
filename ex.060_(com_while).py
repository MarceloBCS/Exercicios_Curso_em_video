cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

n = int(input('Fatorial de qual nº: '))
multiplicador = n
fatorial = 1

while multiplicador > 0:
    print(multiplicador, ' x ' if multiplicador > 1 else ' = ', end=' ')
    fatorial = fatorial * multiplicador
    multiplicador = multiplicador - 1

print('{2}{0}! = {1}{3}'.format(n, fatorial, cor['amarelo'], cor['limp']))

from datetime import date
print('\nProcessado em {}'.format(date.today()))


#solução do professor:
'''n = int(input('digite um número para o fatorial: '))
c = n
f = 1

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))'''


