preco = float(input('\nDiga o Preço do produto: R$ '))

cor = {'red':'\033[1;31m', 'amarela':'\033[1;33m', 'az':'\033[1;34m', 'ver':'\033[1;32m', 'roxo':'\033[1;35m', 'limp':'\033[m'}

op1 = 0.90 * preco
op2 = 0.95 * preco
op3 = preco
op4 = 1.2 * preco

print('\nOpções de pagamento:')
print('[1] à vista em dinheiro ou cheque =================== R$ {:.2f}'.format(op1))
print('[2] á vista no cartão: 5% de desconto =============== R$ {:.2f}'.format(op2))
print('[3] em até 2x no cartão = Preço normal, ou seja, = 2x R$ {:.2f}'.format(op3/2))
print('[4] em 3x ou mais no cartão = 20% de juros')
print('-='*31)

forma = input('Qual é a opção de pagamento desejada? ')

if forma == '1':
    print('\nVc escolheu opção {0} ({2}à vista em dinheiro ou cheque{3}) que tem {2}10% de desconto = R$ {1:.2f}{3}'
          .format(forma, op1, cor['az'], cor['limp']))
elif forma == '2':
    print('\nVc escolheu opção {0} ({2}á vista no cartão{3}) que tem {2}5% de desconto = R$ {1:.2f}{3}'
          .format(forma, op2, cor['ver'], cor['limp']))
elif forma == '3':
    print('\nVc escolheu opção {0} =-> {2}Em 2x no cartão = Preço normal{3}.\n{2}2x R$ {1:.2f}{3} (SEM juros)'
          .format(forma, op3/2, cor['amarela'], cor['limp']))
elif forma == '4':
    print('\nVc escolheu opção {0} =-> Em 3x ou mais no cartão = 20% de juros)'.format(forma))
    parcela = int(input('Quantas parcelas vc deseja dividir? '))
    if parcela >= 3:
        print(' {3}{0} x R$ {1:.2f} = R$ {2:.2f}{4} (com 20% de Juros)'.format(parcela, op4/parcela, op4, cor['red'], cor['limp']))
    else:
        print('\n{}Vc escolheu opção inexistente. Esta opção é APENAS para mais de 3x com juros de 20%{}'.format(cor['roxo'], cor['limp']))
else:
    print('\n{}Vc escolheu opção inexistente. Escolha 1 opção entre [1] até [4]{}'.format(cor['roxo'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today()))
