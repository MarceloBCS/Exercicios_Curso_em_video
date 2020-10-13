cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

media = soma = contador = 0

while True:
    n = int(input('diga um número inteiro ou [999] para parar: '))
    if n == 999:
        break
    soma += n
    contador += 1
print('\nForam regitrados = {3}{0} números{4}, {3}soma = {1}{4} e a {3}média = {2:.1f}{4}'
      .format(contador, soma, soma/contador, cor['amarelo'], cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')
