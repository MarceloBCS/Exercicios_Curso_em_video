n = int(input('\nYoung Grasshopper, Please, tell me one number integer: '))
print('''Qual é a base de conversão:
[1] binário 
[2] octal 
[3] hexadecimal ''')

c = input('\nQual é sua opção? ')

cor = {'red':'\033[1;31m', 'az':'\033[1;34m', 'amarelo':'\033[1;33m', 'limp':'\033[m'}

if c == '1':
    print('\nEm decimal = ', n)
    n = bin(n)
    print(cor['red'], 'Em binário = ', n[2:], cor['limp'])
elif c == '2':
    print('\nEm decimal =', n)
    #n = oct(n)
    print(cor['az'], 'Em octonal = {} '. format(oct(n)[2:]), cor['limp'])
elif c == '3':
    print('\nEm decimal = ', n)
    n = hex(n)
    print(cor['amarelo'], 'Em hexadecimal =', n[2:], cor['limp'])
else:
    print('\nvc {0}escolheu uma opção ERRADA{1}, tente de novo !'.format(cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))