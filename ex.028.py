import random
a = random.randint(0, 5)
print(a) #esta linha só será usada para fazer os testes da lógica

cor = {'az':'\033[1;34m', 'limp':'\033[m', 'red':'\033[1;31m', 'amarelo':'\033[1;33m'}

import time

b = int(input('\nadvinhe o nº que pensei entre 0 e 5? '))

if a == b <= 5:
    print('\nDeixa eu pensar...')
    time.sleep(1)
    print('\no PC escolheu o nº {0} e o seu palpite foi {1}. {2}Logo, vc ganhou!!{3}'.format(a, b, cor['az'], cor['limp']))
elif a != b <= 5:
    print('\nDeixa eu pensar...')
    time.sleep(1)
    print('\no PC escolheu o nº {0} e o seu palpite foi {1}. {2}Logo, vc perdeu!!{3}'.format(a, b, cor['red'], cor['limp']))
else:
    print('\n {}vc escolheu um número acima de 5{}'.format(cor['amarelo'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))















