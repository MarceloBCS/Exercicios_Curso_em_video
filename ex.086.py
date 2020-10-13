l0 = []
l1 = []
l2 = []

for l in range(0, 3):
    for c in range(0,3):
        print('Digite valor ', end='')
        n = int(input(f'[{l},{c}]: '))
        if l == 0:
            l0.append(n)
        elif l == 1:
            l1.append(n)
        elif l == 2:
            l2.append(n)

#Outra versão para colocar na tela
#print('-='*10)
#print(f'[ {l0[0]:^6} ] [ {l0[1]:^6} ] [ {l0[2]:^6} ]')
#print(f'[ {l1[0]:^6} ] [ {l1[1]:^6} ] [ {l1[2]:^6} ]')
#print(f'[ {l2[0]:^6} ] [ {l2[1]:^6} ] [ {l2[2]:^6} ]')

print('-='*12)
for c in range(0, 3):
    print(f'[{l0[c]:^5}]', end='')
print('')
for c in range(0, 3):
    print(f'[{l1[c]:^5}]', end='')
print('')
for c in range(0, 3):
    print(f'[{l2[c]:^5}]', end='')

from datetime import date
print(f'\n\nProcessado em {date.today()}')