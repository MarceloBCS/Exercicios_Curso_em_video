from random import randint, sample
from time import sleep

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}
jogo = []

print('-'*37)
print(' '*13, 'Mega Sena')
print('-'*37)

j = int(input('Qtos jogos vc quer quer eu sorteie? '))
print('-='*4, f'Sorteando {j} JOGOS', '-='*5)
for c in range(1, j+1):
    n = sample(range(1, 60), 6)     #função Sample já é uma lista com 1º parâmetro o universo possível e o 2º, a Qde
    n.sort()
    jogo.append(n[:])
    sleep(1)
    print(f'jogo {c:>2}', cor['amarelo'], n, cor['limp'])
    del n[:]
sleep(1)
print('-='*5, '< Boa Sorte! >', '-='*6)
sleep(1)
print('\nTodas as cartelas = ', cor['amarelo'], jogo, cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')
