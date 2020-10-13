cor = {'red':'\033[1;31m', 'limp':'\033[m'}

l0 = []
l1 = []
l2 = []
soma_par = 0

for l in range(0, 3):
    for c in range(0, 3):
        print('Digite p valor: ', end='')
        num = int(input(f'[{l}, {c}]: '))
        if l == 0:
            l0.append(num)
        elif l == 1:
            l1.append(num)
        elif l == 2 :
            l2.append(num)
        if num % 2 == 0:
            soma_par += num

print('-='*12)
print(f'[ {l0[0]} ] [ {l0[1]} ] [ {l0[2]} ]')
print(f'[ {l1[0]} ] [ {l1[1]} ] [ {l1[2]} ]')
print(f'[ {l2[0]} ] [ {l2[1]} ] [ {l2[2]} ]')
print('-='*12)

print('A {1}soma{2} dos valores {1}pares{2} é {1}{0}{2}'.format(soma_par, cor["red"], cor["limp"]))
print('A {1}soma{2} dos valores da {1}3º coluna{2} é {1}{0}{2}'. format((l0[2]+l1[2]+l2[2]), cor["red"], cor["limp"]))
print('O {1}maior{2} valor da {1}2º linha{2} é {1}{0}{2}'.format(max(l1), cor["red"], cor["limp"]))

from datetime import date
print(f'\nProcessado em {date.today()}')
