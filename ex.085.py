cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

num = [[], []]

for c in range(1,8):
    n = int(input(f'{c}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f'\nEm forma de lista, os valores digitados foram: {cor["amarelo"]}{num}{cor["limp"]}')
print(f'Os {cor["amarelo"]}pares = {num[0]}{cor["limp"]}')
print(f'Os {cor["amarelo"]}ímpares = {num[1]}{cor["limp"]}')

from datetime import date
print(f'\nProcessado em {date.today()}')

