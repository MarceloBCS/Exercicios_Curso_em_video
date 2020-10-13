e = str(input('\ndiga [C] para entrar com graus Celsius ou [F] para entrar em graus Fahrenheit '))

cor = {'azul':'\033[1;34m', 'amarelo':'\033[1;33m', 'red':'\033[1;31m','limp':'\033[m'}

if e == 'C' or e =='c':
    temperatura = float(input('\n{0}Diga a temperatura em [ºC]{1}: '.format(cor['azul'], cor['limp'])))
    tf = temperatura*9/5+32
    print('\na temperatura {2}{0}ºC{4} será igual a {3}{1:.1f}ºF{4}'.format(temperatura, tf, cor['azul'], cor['amarelo'], cor['limp']))
elif e == 'F' or e == 'f':
    temperatura = float(input('\n{0}Diga a temperatura em [ºF]{1}: '.format(cor['amarelo'], cor['limp'])))
    tc = (temperatura-32)/9*5
    print('\na temperatura {2}{0}ºF{4} será igual a {3}{1:.1f}ºC{4}'
          .format(temperatura, tc, cor['amarelo'], cor['azul'], cor['limp']))
else:
    print('\n{}Vc não escolheu a unidade de temperatura corretamente, sua Mula !!!{}'.format(cor['red'], cor['limp']))
    print('\ndiga [C] para entrar com graus Celsius ou [F] para entrar em graus Fahrenheit ')

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


