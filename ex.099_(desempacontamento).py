from time import sleep

cor = {'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'limp':'\033[m'}

def maior(*num):
    m = len('Analisando os valores passados...')
    print('='*m)
    print('Analisando os valores passados...')
    for c in num:
        print(cor['amarelo'], c, cor['limp'], end='|')
        sleep(.2)
    for c in range(0, len(num)):
        if c == 0:
            maximo = num[0]
        elif c > 0:
            if num[c] > num[c-1]:
                maximo = num[c]
    print(f'\nForam informados {cor["amarelo"]}{len(num)} valores{cor["limp"]} ao todo')
    print('O {0}maior valor{1} gerado ='.format(cor['amarelo'], cor['limp']),
          f'{cor["amarelo"]}{maximo}{cor["limp"]}' if num != () else '{}NÃO FOI INFORMADO QUALQUER VALOR{}'.format(cor['red'], cor['limp']))


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

from datetime import date
print(f'\nProcessado em {date.today()}')