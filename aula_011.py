print('\n\033[7;30;41mOlá Mundo\033[m')
print('\033[0;31mOlá Mundo\033[m')

a = 3
b = 4
c = 'Marcelo'

cores = {'limpa':'\033[m', 'vermelho':'\033[4;31m', 'azul':'\033[4;34m', 'amarelo':'\033[4;33m', 'verde':'\033[4;32m'}

print('\nos valores são \33[1;33m{0}\33[m e \33[1;34m{1}\33[m'.format(a, b))

print('os valores são {0}{1}{2} e {3}{4}{5}, {6}{7}{8} !!! '.format('\033[4;31m', a, '\033[m', '\033[4;32m', b, '\033[m', '\033[4;33m', c, '\033[m)'))

print('os valores são {0}{1}{2} e {3}{4}{2}, {5}{6}{2} !!! '.format('\033[4;31m', a, '\033[m', '\033[4;32m', b, '\033[4;33m', c))

print('os valores são {0}{1}{2} e {0}{3}{2} , {0}{4}{2}'.format('\033[4;31m', a, '\033[m', b, c ))

print('\nos valores são {0}{1}{2} e {3}{4}{2}, {5}{6}{2}'.format(cores['vermelho'], a, cores['limpa'], cores['verde'], b, cores['azul'], c))



import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))














