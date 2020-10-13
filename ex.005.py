n = int(input('\nYoung grasshopper, diga o nº base: '))

cor = {'azul':'\033[1;34m', 'limp':'\033[m'}

print('\n antecessor será {2}{0:^9}{4}, \n o nº base será {1:|^10} \n e o sucessor será {2}{3:^5}{4}'.format(n-1, n, cor['azul'], n+1, cor['limp']))


import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))







