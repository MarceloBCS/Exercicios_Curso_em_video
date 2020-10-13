from random import randint
from operator import itemgetter
from time import sleep

jogo = {'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6)}
print('-='*20)
print(jogo)

print('-='*20)
print('--- valores sorteados ---')
sleep(.5)
for key, val in jogo.items():
    print(f'{key} tirou {val} no dado')
    sleep(.5)

print('='*29)

#itemgetter(0) é ordenar pela chave e (1) é pelo valor
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking ordenado = ', ranking)

print('='*29)
print('=== RANKING DOS JOGADORES ===')
sleep(.5)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]} ')
    sleep(.5)


