from random import sample
from datetime import date
from time import sleep

cor = {'red':'\033[1;31m', 'limp':'\033[m', 'az':'\033[1;34m'}


def maior(k):
    c = len('Analisando os valores passados...')
    print('=' * c)
    print('Analisando os valores passados...')
    if k == 0:
        n = []
    if k > 0:
        n = sample(range(0, 10), k)
    for x in range(0, len(n)):
        sleep(.2)
        print(cor['red'], f'{n[x]}', cor['limp'], end='|')
    print(f'\nForam informados {cor["az"]}{len(n)} valores{cor["limp"]} ao todo')
    print('O {}maior{} valor gerado foi'.format(cor['az'], cor['limp']),
          f'{cor["az"]}{max(n)}{cor["limp"]}' if k > 0 else f'{cor["az"]}0{cor["limp"]}')
    print()


maior(6)
maior(3)
maior(2)
maior(1)
maior(0)

print(f'\nProcessado em {date.today()}')