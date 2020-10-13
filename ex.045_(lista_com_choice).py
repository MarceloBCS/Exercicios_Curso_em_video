import random, datetime, time

s = ['pedra', 'papel', 'tesoura']

cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'limp':'\033[m'}

pc = random.choice(s)
print(pc) #usado apenas para fazer testes do que o PC escolheu

jogador = input('\nEscolha Pedra ou Papel ou Tesoura: ').lower().strip()

if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    print('-='*20)
    print('Jo')
    time.sleep(.5)
    print('ken')
    time.sleep(.5)
    print('po')
    time.sleep(1)
    print('-='*20)

    if jogador == pc:
        print('O {1}Computador{2} e {1}Jogador{2} jogaram {1}{0}{2}.\n{3}\nLogo, {1}ninguém ganhou{2}'
              .format(jogador, cor['amarelo'], cor['limp'], '-='*20))
    elif (jogador == 'tesoura' and pc != 'pedra') or (jogador == 'pedra' and pc != 'papel') or (jogador == 'papel' and pc != 'tesoura'):
        print('O {2}computador{4} jogou {2}{0}{4} e {3}Jogador{4} jogou {3}{1}{4}. \n{5}\nLogo, {3}JOGADOR Venceu{4}. Parabéns !!!'
              .format(pc, jogador, cor['red'], cor['az'], cor['limp'], '-='*20))
    else:
        print('O {2}Computador{4} jogou {2}{0}{4}\n{3}Jogador{4} jogou {3}{1}{4}.\n{5}\nLogo, o {2}Computador VENCEU{4} !!!'
              .format(pc, jogador, cor['red'], cor['az'], cor['limp'], '-='*20))
else:
    print('\n{}Vc escolheu uma opção inexistente. Tente de novo'.format(cor['red'], cor['limp']))

print('\nProcessado em {}'.format(datetime.date.today()))