from random import randint
from time import sleep

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

def sorteio():
    print(f'Sorteando 5 valores da lista:', end='')
    for c in range(1, 6):
        n = randint(0, 9)
        numeros.append(n)
        print(cor['amarelo'], n, cor['limp'], end='')
        sleep(.2)
    print()


def somaPar():
    som = 0
    print('elemento(s) par(es): ', end='')
    for valor in numeros:
        if valor % 2 == 0:
            print(cor['amarelo'], valor, cor['limp'], end='|')
            som += valor
            sleep(.2)
    print(f'\nA soma dos elementos pares =', cor['amarelo'], som, cor['limp'])


numeros = []
sorteio()
somaPar()

from datetime import date
print(f'\nProcessado em {date.today()}')