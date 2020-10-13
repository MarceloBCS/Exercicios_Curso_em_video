cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

contador = 1
lista = []
while True:
    print(cor['amarelo'], '-='*13, cor['limp'])
    print('diga o ', end='')
    n = int(input(f'{contador}º item da lista: '))
    if n not in lista:
        lista.append(n)
        contador += 1
        print('valor adicionado com sucesso...')
    else:
        print('item já consta na lista')
    fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        fim = input('Dado inválido. Quer continuar? [S/N] ').strip().upper()
    if fim == 'N':
        break
lista.sort()
print('\nos valores digitados (sem repetição) foi:', cor['amarelo'], lista, cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')

