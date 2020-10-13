s = float(input('Qual é o seu salário: R$ '))

cor = {'az':'\033[1;34m', 'limp':'\033[m', 'amarelo':'\033[1;33m'}

if s > 1250:
    s_novo = s * 1.1
    print('\nSeu salário aumentará de R$ {0:^10.2f} para R$ {1:^10.2f} - {2}aumento de 10%{3}'.format(s, s_novo, cor['amarelo'], cor['limp']))
else:
    s_novo = s * 1.15
    print('\nSeu salário aumentará de R$ {0:^10.2f} para R$ {1:^10.2f} - {2}aumento de 15%{3}'.format(s, s_novo, cor['az'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


