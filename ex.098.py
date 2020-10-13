from time import sleep

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

def contador(inicio, fim, passo):
    print(f'A contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if inicio > fim:
        fim -= 1
        if passo == 0:
            passo = -1
        elif passo > 0:
            passo = passo * (-1)
    elif inicio <= fim:
        fim += 1
        if passo == 0:
            passo = 1
        elif passo < 0:
            passo = abs(passo)
    for c in range(inicio, fim, passo):
        print(cor['amarelo'], c, cor['limp'], end=' | ', flush=True) #Não mudou nada a contagem de flush (para eliminar
                                                                     #a espera de tela, antes de começar o print)
        sleep(.5)
    print()


def lin(txt):
    c = len(txt)
    print()
    print('='*c)
    print(txt)
    print('='*c)


lin('De 1 até 10, de 1 em 1:')
contador(1, 10, 1)

lin('De 10 até 0, de 2 em 2:')
contador(10, 0, -2)

lin('Agora é a sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))

contador(inicio, fim, passo)

from datetime import date
print(f'\nProcessado em {date.today()}')