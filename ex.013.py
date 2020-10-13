s = float(input('\nYoung Grasshopper, diga o seu salário: R$ '))
ns = s * 1.15

cor = {'amarelo':'\033[1;31m', 'azul':'\033[1;34m', 'limp':'\033[m'}

print('\nCom o {2}Aumento de 15%{4}, seu salário passará de R$ {0:^10.2f} para {3}R$ {1:^10.2f}{4}'
      .format(s, ns, cor['amarelo'], cor['azul'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
