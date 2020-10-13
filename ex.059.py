import datetime

n1 = float(input('insira o 1º número: '))
n2 = float(input('insira o 2º número: '))

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

c = 0
while c == 0:
    print('-='*15)
    opcao = int(input('''Digite uma das opções abaixo:
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa  ==> '''))
    if opcao == 1:
        soma = n1 + n2
        print('{3}{0} + {1} = {2}{4}'.format(n1, n2, soma, cor['amarelo'], cor['limp']))
    elif opcao == 2:
        produto = n1 * n2
        print('{3}{0} x {1} = {2}{4}'.format(n1, n2, produto, cor['amarelo'], cor['limp']))
    elif opcao == 3:
        maior = n1
        if n2 > maior:
            maior = n2
            print('{3}{0} > {1} --→ o maior é {2}{4}'.format(n2, n1, maior, cor['amarelo'], cor['limp']))
        else:
            print('{3}{0} > {1} --→ o maior é {2}{4}'.format(n1, n2, maior, cor['amarelo'], cor['limp']))
    elif opcao == 4:
        print(cor['red'])
        n1 = float(input('diga 1º novo número: '))
        n2 = float(input('diga 2º novo número: '))
        print(cor['limp'])
    elif opcao == 5:
        c = 1

print('\nProcessado em {}'.format(datetime.date.today()))