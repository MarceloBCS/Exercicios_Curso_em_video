cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'az':'\033[1;34m'}

tot = 0
cartel = {}
lista_gol = []
cartel['nome'] = input('Nome: ').strip().title()

n = int(input(f'Qtos partidas {cartel["nome"]} jogou? '))
for c in range(1, n+1):
    gol = int(input(f'Qtas gols na partida {c} '))
    tot += gol
    lista_gol.append(gol)

print('-='*20, cor['amarelo'])
cartel['gols'] = lista_gol.copy()
cartel['total'] = tot
print(cartel, cor['limp'])
print('-='*20)

print(cor['az'], end='')
print(f'Nome......... = {cartel["nome"]}')
print(f'gols......... = {lista_gol}')
print(f'Total de gols = {tot}', cor['limp'])
print('-='*20)

print(f'O jogador {cartel["nome"]} jogou {cor["amarelo"]}{n} partidas{cor["limp"]}')

for k, v in enumerate(lista_gol):
    print('=> Na {2}partida {0}{3}, fez {2}{1} gols{3}'.format(k, v, cor['amarelo'], cor['limp']))

print(f'Foi um total de {cor["amarelo"]}{tot} gols{cor["limp"]}')

from datetime import date
print(f'\nProcessado em {date.today()}')
