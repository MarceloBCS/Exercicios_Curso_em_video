nome = input ('Qual é o seu nome, Young Grasshopper??? ')

cor = {'amarelo':'\033[1;33m', 'azul':'\033[1;36m', 'verm':'\033[1;32m', 'limp':'\033[m'}


print ('\nOlá Sr', cor['amarelo'], nome , cor['limp'], 'seja muito bem vindo!!!', end=' ')
print ('Que bom que vc digitou o seu nome, {}'.format(nome))

n1 = int(input ('\nDigite o 1º número, {} '.format(nome)))
n2 = int(input ('digite o 2º número, {} '.format(nome)))
soma = (n1 + n2)

print ('\na soma dos números {0}{1}{2} e {3}{4}{2}, será: {5}{6}{2}'.format(cor['amarelo'], n1, cor['limp'], cor['verm'], n2, cor['azul'], soma))

import datetime
print('\nprograma executado em {}'.format(datetime.date.today().today()))


