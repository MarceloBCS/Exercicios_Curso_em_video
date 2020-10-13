cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'limp':'\033[m'}

reg = []
cartel = {}
lista_gol = []
while True:
    cartel['nome'] = input('Nome do jogador: ').strip().title()
    tot_gol = 0
    n = int(input(f'Qtas partidas {cartel["nome"]} jogou? '))
    for c in range(1, n+1):
        gol = int(input(f'Qtos gols na partida {c}? '))
        tot_gol += gol
        lista_gol.append(gol)
    cartel['gols'] = lista_gol[:]
    cartel['total'] = tot_gol
    print(cartel)
    reg.append(cartel.copy())
    lista_gol = []
    print('-='*20)
    fim = input('Quer continuar: [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        print(cor['red'], 'Dados inválidos. ', cor['limp'], end='')
        fim = input('Quer continuar: [S/N] ').strip().upper()[0]
    if fim == 'N':
        break
    print('-='*20)

print('-='*60)
print(reg)
print('-='*60)

print('-'*50)
print('Cod', ' ', 'nome', ' '*7, 'gols', ' '*13, 'total')
print('-'*50)
for c in range(0, len(reg)):
    print('{4}{0:<4} {1:<12} {2:<20} {3:<15}{5}'.format(c, reg[c]['nome'], str(reg[c]['gols']), reg[c]['total'],
          cor['amarelo'], cor['limp']))

#for k, v in enumerate(reg):        #mesma coisa que o código da linha 36. Utilizando "STR" transforma lista em string
#    print(f'{k:<3}', end='  ')
#    for key in v.values():
#        print(f'{str(key):<17}', end='')
#   print()
print('-'*50)

while True:
    mostra = int(input('Mostrar dados de qual jogador? ([999] para sair) '))
    if mostra == 999:
        break
    while mostra >= len(reg) and mostra != 999:
        print(cor['red'], 'Dado inválido. ', cor['limp'], end='')
        mostra = int(input('Mostrar dados de qual jogador? ([999] para sair) '))
    for k, v in enumerate(reg):
        if mostra == k:
            print('-'*50)
            print(f'-- levantamento do {cor["amarelo"]}jogador {reg[k]["nome"]}{cor["limp"]}:')
            for c in range(0, len(reg[k]['gols'])):
                print(cor['amarelo'], f'No jogo {c} fez {reg[k]["gols"][c]} gols', cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')