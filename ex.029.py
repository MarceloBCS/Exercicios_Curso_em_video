v = int(input('Diga a velocidade [km/h] : '))

cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'limp':'\033[m'}

if 40 < v <= 80:
    print('\n{}*** continue assim, dirigindo com cuidado ***{}'.format(cor['az'], cor['limp']))
elif v>80:
    p = (v-80)*7
    print('\nSua velocidade é {0} Km/h e vc excedeu o limite local de 80km/h'.format(v))
    print('\n{1}Sua multa será de R${0}{2}'.format(p, cor['red'], cor['limp']))
else:
    print('\n{}ACELERA seu roda presa !!!!!{}'.format(cor['amarelo'], cor['limp']))
print('\nSe Beber não dirija !')

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))






