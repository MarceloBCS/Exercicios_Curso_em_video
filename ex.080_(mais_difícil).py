cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

lis = []
for c in range(1,6):
    print('-='*20)
    n = int(input(f'diga o {c}º número: '))

    if c == 1:
        lis.append(n)
        print(f'Adicionado na posição 0')
        print(lis)

    elif c >= 2:
            if n <= lis[0]:
                lis.insert(0, n)
                print(f'Adicionado com Sucesso na posição 0')
                print(lis)
            elif n >= lis[-1]:
                lis.append(n)
                print(f'Adicionado com Sucesso ao final da lista')
                print(lis)
            else:
                for r in range(1, c):
                        if n <= lis[r]:
                            lis.insert(r, n)
                            print(f'Adicionado com Sucesso na posição {r}')
                            print(lis)
                            break
print('-='*20)
print('A lista ordenada é: {}{}{}'.format(cor['amarelo'], lis, cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')
