cor = {'az':'\033[1;34m', 'red':'\033[1;31m', 'limp':'\033[m'}

vitoria = soma = jogador_num = 0
perder = False
jogador_tipo = ''

while perder == False:
    from random import randint, seed
    seed()
    pc = randint(1, 10)
    #print(pc) #apenas para teste
    print('*'*45)
    print('*** Jogo do Par ou Ímpar contra a máquina ***')
    print('*'*45)
    jogador_num = int(input('Diga um número entre 1 a 10: '))
    jogador_tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print('-'*45)

    soma = pc + jogador_num
    if soma % 2 == 0 and jogador_tipo == 'P':
        vitoria += 1
        print('PC jogou {0}\nJogador jogou {1}. A Soma é {2} (PAR). {3}Jogador venceu!{4}'
              .format(pc, jogador_num, soma, cor['az'], cor['limp']))
    elif soma %2 != 0 and jogador_tipo == 'I':
        vitoria += 1
        print('PC jogou {0}\nJogador jogou {1}. A Soma é {2} (ÍMPAR). {3}Jogador venceu!{4}'
              .format(pc, jogador_num, soma, cor['az'], cor['limp']))
    elif soma %2 == 0 and jogador_tipo == 'I':
        print('PC jogou {0} e Jogador jogou {1}. A Soma é {2} (PAR). {3}PC venceu!{4}'
              .format(pc, jogador_num, soma, cor['red'], cor['limp']))
        perder = True
    elif soma % 2 != 0 and jogador_tipo == 'P':
        print('PC jogou {0} e Jogador jogou {1}. A Soma é {2} (ÍMPAR). {3}PC venceu!{4}'
              .format(pc, jogador_num, soma, cor['red'], cor['limp']))
        perder = True

print(cor['red'], f'\nGame Over, Player 1!!! ....... Vc ganhou {vitoria} vezes')

