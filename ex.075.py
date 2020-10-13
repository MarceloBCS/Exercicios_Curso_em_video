cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'limp':'\033[m'}

#Outra forma de fazer:
#num = (int(input('1º número inteiro: ')), int(input('2º número inteiro: ')),
#       int(input('3º número inteiro: ')), int(input('4º número inteiro: ')),)

#Forma como eu fiz:
n1 = int(input('\nDiga o 1º número inteiro: ')),
n2 = int(input('Diga o 2º número inteiro: ')),
n3 = int(input('Diga o 3º número inteiro: ')),
n4 = int(input('Diga o 4º número inteiro: ')),
t = n1 + n2 + n3 + n4

print('\nos valores digitados foram {1}{0}{2}'.format(t, cor['red'], cor['limp']))
print('\nA)  {1}#9{2} apareceu {1}{0} vezes{2}'.format(t.count(9), cor['amarelo'], cor['limp']))

if 3 in t:
    print('B)  o {1}elemento #3{2} apareceu na {1}posição {0}{2} '.format(t.index(3)+1, cor['amarelo'], cor['limp']))
else:
    print('B)', cor['red'], 'Não existe elemento #3 nesta tupla', cor['limp'])
#print(f'B) #3 na {t.index(3)+1}º posição' if 3 in t else 'B) O elemento #3 não está na tupla')

contador_pares = 0
print('C)  Os números pares são: ', cor['amarelo'], end='')
#for c in range(0,4):                #Poderia ter usado: for c in t:
#    if t[c] % 2 == 0:               #                       if c % 2 == 0:
#        contador_pares += 1         #                       contador_pares += 1
#        print(f'{t[c]}', end=' | ') #                       print(f'{c}', end=' | ')

#A forma abaixo só pode usar um único elemento da tupla por vez. Se precisar "somar" o índice (por exemplo), ele dá erro
#pq o "c" não é um número inteiro que possa fazer operações matemáticas. Neste caso, o for c range() é mais versátil.
for c in t:
    if c % 2 == 0:
        contador_pares += 1
        print(f'{c}', end=' | ')

print(cor['limp'])
print('    Identificado(s) {0}{1} nº par(es){2}'.format(cor['amarelo'], contador_pares, cor['limp']))

from datetime import date
print(f'\nProcessador em {date.today()}')





