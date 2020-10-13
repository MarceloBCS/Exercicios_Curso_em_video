cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

futebol = ('INTERNACIONAL', 'SÃO PAULO', 'VASCO', 'FLUMINENSE', 'ATLÉTICO-MG', 'PALMEIRAS', 'FORTALEZA',
            'BAHIA', 'FLAMENGO', 'SANTOS', 'CEARÁ', 'GRÊMIO', 'ATHLETICO-PR', 'CORITIBA', 'BOTAFOGO',
            'CORINTHIANS', 'BRAGANTINO', 'GOIÁS', 'SPORT','ATLÉTICO-GO')
print(f'8º posição: {futebol[7]}')
print('\n','-='*30)
print(f' Estão jogando {len(futebol)} clubes no Brasileirão 2020')
print('-='*30)
for pos, nome in enumerate (futebol):
    print(f'{pos+1:>2}º = {nome}')

print('-='*30)
print(cor['amarelo'], f'A) Os 5 primeiros são:', cor['limp'])
for c in range(0,5):
    print(f'{futebol[c]}', end=' | ')
print('\n', f'{futebol[0:6]}', end= ' | ')    #forma mais enxuta que a de cima, mas "printa" com parênteses
print('\n', '-='*30)

print(cor['amarelo'], 'B) Os últimos 4 da tabela são:', cor['limp'])
for c in range(-4,0):
    print(f'{futebol[c]}', end=' | ')
print('\n', f'{futebol[-4:]}', end=' | ')      #forma mais enxuta que a de cima, mas "printa" com parênteses
print('\n','-='*30)

print(cor['amarelo'], 'C) Colocando os times em ordem alfabética: ', cor['limp'])
print(sorted(futebol))
print('-='*30)

print(cor['amarelo'], 'D) Em que posição está o Time do Bahia? ', cor['limp'])
print('Bahia está na posição: #{}'.format(futebol.index('BAHIA')+1))

from datetime import date
print(f'\nProcessado em {date.today()}')
