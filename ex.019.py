a1 = input('diga o nome do aluno 1: ')
a2 = input('diga o nome do aluno 2: ')
a3 = input('diga o nome do aluno 3: ')
a4 = input('diga o nome do aluno 4: ')

cor = {'azul':'\033[1;34m', 'limp':'\033[m', 'amarelo':'\033[1;33m'}

import random

s = [a1, a2, a3, a4]

print('\n{1}o 1º sorteado = {0}{2}'.format(random.choice(s), cor['azul'], cor['limp']))

# trocando a ordem dos alunos (NÃO pode "printar" junto com o Shuffle ( print(random.shuffle(s)) ), pq dá resultado NONE.
random.shuffle(s)
print('\n{0}Mudando a ordem dos alunos, teremos:{1} {2} '.format(cor['amarelo'], cor['limp'], s))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
