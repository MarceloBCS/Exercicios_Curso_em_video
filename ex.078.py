cor = {'az':'\033[1;34m', 'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'verde':'\033[1;32m', 'limp':'\033[m'}

lista_num = []

for c in range(1,6):
    print(f'{c}º ', end='' )
    n = int(input('número: '))
    lista_num.append(n)
print(lista_num)

menor = min(lista_num)
maior = max(lista_num)

print('\nO {3}menor{6} é {3}{0}{6}, com 1º ocorrência {4}posição {1}{6}. Ele apareceu {5}{2} vez(es){6}'
      .format(menor, lista_num.index(menor), lista_num.count(menor), cor['az'], cor['amarelo'], cor['red'], cor['limp']))

print('Posições: ', end='')
for pos, valor in enumerate(lista_num):
    if valor == menor:
        print(cor['verde'], pos, cor['limp'], end='|')

print('\n\nO {3}maior{6} é {3}{0}{6}, com 1º ocorrência na {4}posição {1}{6}. Ele apareceu {5}{2} vez(es){6}'
      .format(maior, lista_num.index(maior), lista_num.count(maior), cor['az'], cor['amarelo'], cor['red'], cor['limp']))

print('Posições: ', end='')
for pos, valor in enumerate(lista_num):
    if valor == maior:
        print(cor['verde'], pos, cor['limp'], end='|')

from datetime import date
print(f'\n\nProcessado em {date.today()}')

