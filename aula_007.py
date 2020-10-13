nome = input ('Qual é o seu nome ? ')
print ('Seja bem vindo {:^20}, prazer na sua visita  !!!'.format(nome))
print ('Seja bem vindo {:<20}, prazer em te conhecer !!!'.format(nome))
print ('Seja bem vindo {:>20}, prazer em te conhecer !!!'.format(nome))
print ('Seja bem vindo {:=^20}, prazer na sua visita !!!'.format(nome))

n1 = int(input('Diga o 1º número: '))
n2 = int(input('Diga o 2º número: '))
s = n1 + n2
p = n1 * n2
e = n1 ** n2
d = n1 / n2
inteiro = n1 // n2
r = n1 % n2
print('a soma do {0} e {1} será {2} e o produto de {0} e {1} será {3}'.format(n1, n2, s, p), end='')
print('. A exponenciação de {0} e {1} será {2} e \n a divisão de {0} e {1} será {3:.4f} \n '.format(n1, n2, e, d))
print('Como a divisão de {0} e {1} é {2:.2f}, \n o inteiro da divisão de {0} e {1} será {3} \n e o resto da divisão de {0} e {1} será {4}'.format(n1, n2, d, inteiro, r))












