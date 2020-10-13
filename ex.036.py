v = float(input('\nQual é o valor da casa = R$ '))
s = float(input('Qual é o salário mensal = R$ '))
t = int(input('Em quantos anos vc vai pagar = '))

cor = {'red':'\033[1;31m', 'limp':'\033[m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m'}

p = v / t / 12

if p > 0.3 * s:
    print('\nO valor {3}{0:.0f}{4} em {3}{1}{4} anos gerará uma prestação de : R$ {3}{2:.2f}{4}'.format(v, t, p, cor['red'], cor['limp']))
    print('infelizmente, o valor da prestação é muito alto para sua renda.')
    print(cor['red'], 'Financiamento negado !', cor['limp'])
elif p == 0.3 * s:
    print('\no valor {3}{0:.0f}{4} em {3}{1}{4} anos gerará uma prestação de = R$ {3}{2:.2f}{4}'.format(v, t, p, cor['amarelo'], cor['limp']))
    print(cor['az'], 'Prestação no limite da sua renda, mas foi Aprovado !!!', cor['limp'])
else:
    print('\nprestação {:.2f} é adequada e menor que 30% da sua renda de R$ {:.2f} por mês'.format(p, s))
    print(cor['az'],'Financiamento aprovado !', cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))

