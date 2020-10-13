cor = {'az':'\033[1;34m', 'limp':'\033[m'}


def ficha(nome='', gol=''):
    if nome == '':
        nome = 'DESCONHECIDO'
    if not gol.isdigit():
        gol = 0
    print('O jogador {2}{0}{3} fez {2}{1} gols{3} no campeonato'.format(nome, gol, cor['az'], cor['limp']))


print('-'*34)
nome = input('Nome do Jogador: ').strip().title()
gol = input('Nº de gols: ').strip()
c = len(nome) + len(gol) + 34
print('-'*c)
ficha(nome, gol)

from datetime import date
print(f'\nProcessado em {date.today()}')



