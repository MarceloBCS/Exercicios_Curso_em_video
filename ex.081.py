cor = {'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'limp':'\033[m'}

c = 0
l = []
while True:
    c += 1
    print('-='*12)
    print('diga o ', end='')
    n = int(input(f'{c}º número: '))
    l.append(n)
    print(l)
    fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        print('Não entendi a sua vontade. ', end='')
        fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    if fim == 'N':
        break
print('-='*20)
print('Foram digitados {1}{0} elementos{2}'.format(c, cor['amarelo'], cor['limp']))

l.sort(reverse=True)
print('\nA lista em ordem {1}decrescente{2} é : {1}{0}{2}'.format(l, cor['amarelo'], cor['limp']))

if 5 in l:
    print('\nO {2}elemento #5{3} foi encontrado na lista em {2}{0} ocorrência(s){3}, sendo a 1º vez na {2}posição #{1}{3}'
          .format(l.count(5), l.index(5), cor['amarelo'], cor['limp']))
    print('As posições do elemento 5 foram: ', end='')
    for pos, v in enumerate(l):
        if v == 5:
            print(cor['amarelo'], f'{pos}', cor['limp'], end='|')
else:
    print('\nO {}elemento #5 NÃO foi encontrado{} na lista'.format(cor['red'], cor['limp']))
print('\n', '-='*20)

from datetime import date
print(f'\nProcessado em {date.today()}')

