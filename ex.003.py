n1 = int(input ('Digite o 1º número: '))
n2 = float(input ('digite o 2º número: '))
s1 = n1 + n2

cor = {'amarelo':'\033[1;33m', 'verm':'\033[1;31m', 'roxo':'\033[1;35m', 'limp':'\033[m'}

print ('\na soma entre {0}{1}{2} e {3}{4}{2} é: {5}{6}{2}'.format(cor['amarelo'], n1, cor['limp'], cor['verm'], n2, cor['roxo'], s1))

n3 = float (input('\nqual é o número, Young Grasshopper? '))
n4 = int (input('qual é o outro número???? '))
s2= n3 + n4

print ('\nA soma do {0} e {1} será = {2}{3}{4}'.format (n3, n4, cor['roxo'], s2, cor['limp']))

p1 = s1*s2
print ('o produto das somas {0} e {1} será EXATAMENTE {2}{3}{4}'.format (s1, s2, cor['verm'], p1, cor['limp']))

import datetime
print('\nPrograma executado em {}'.format(datetime.date.today().today()))







