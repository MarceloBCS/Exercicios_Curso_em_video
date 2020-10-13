cor = {'ver':'\033[1;36m', 'limp':'\033[m'}

from random import randint

d1 = randint(1, 6)

d2 = randint(1, 6)
while d2 == d1:
    d2 = randint(1, 6)

d3 = randint(1, 6)
while d3 == d1 or d3 == d2:
    d3 = randint(1, 6)

d4 = randint(1, 6)
while d4 == d1 or d4 == d2 or d4 == d3:
    d4 = randint(1, 6)

from time import sleep
jogo = {'j1':d1, 'j2':d2, 'j3':d3, 'j4':d4}
print(f'o dicionário é = {jogo}')
print('\n', cor['ver'], '-='*5, 'valores sorteados', '-='*5, cor['limp'])
sleep(1)
print(f'jogador_1 tirou {d1} no dado')
sleep(1)
print(f'jogador_2 tirou {d2} no dado')
sleep(1)
print(f'jogador_3 tirou {d3} no dado')
sleep(1)
print(f'jogador_4 tirou {d4} no dado')
sleep(1)
print('', cor['ver'], '-='*4, 'Ranking dos Jogadores', '-='*4, cor['limp'])

lugar = []
for v in jogo.values():
    lugar.append(v)
lugar.sort(reverse=True)
#print('ordenados =', lugar)

for k, v in jogo.items():
    if v == lugar[0]:
        print(f'1º lugar: {k} que tirou {lugar[0]}')

for k, v in jogo.items():
    if v == lugar[1]:
        print(f'2º lugar: {k} que tirou {lugar[1]}')

for k, v in jogo.items():
    if v == lugar[2]:
        print(f'3º lugar: {k} que tirou {lugar[2]}')

for k, v in jogo.items():
    if v == lugar[3]:
        print(f'4º lugar: {k} que tirou {lugar[3]}')

from datetime import date
print(f'\nProcessado em {date.today()}')