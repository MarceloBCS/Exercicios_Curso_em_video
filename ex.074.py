cor = {'az':'\033[1;34m', 'limp':'\033[m', 'red':'\033[1;31m'}

from random import randint, seed
seed()
t1 = randint(1,10),
t2 = randint(1,10),
t3 = randint(1,10),
t4 = randint(1,10),
t5 = randint(1,10),
t = t1 + t2 + t3 + t4 + t5

#outra forma de fazer
tupla_mumerica = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(cor['red'],'\n', f'Tupla numérica é {tupla_mumerica}')
print(f' O menor elemento é {min(tupla_mumerica)} e o maior elemento é {max(tupla_mumerica)}', cor['limp'])

menor = min(t)
maior = max(t)

print('\n', f'os números gerados foram: {t1[0]}, {t2[0]}, {t3[0]}, {t4[0]}, {t5[0]}')   #"printa" SEM parênteses
print('\nA tupla gerada foi {0}{1}{2}'.format(cor['az'], t, cor['limp']))               #"printa" COM parênteses
print('O {2}menor{3} elemento é: {2}{0}{3}\nO {2}maior{3} elemento é: {2}{1}{3}'.format(menor, maior, cor['az'], cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')



