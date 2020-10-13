a = int(input('diga o 1º termo da PA: '))
r = int(input('diga a razão da PA: '))
n = int(input('diga quantos termos terá esta PA: '))

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

contador = 1
tot = 0
while contador < n+1:
    while contador < n+1:
        print(cor['amarelo'], a, cor['limp'], '→' if contador < n else '\033[1;31m pausa \033[m', end='')
        a += + r
        contador += +1
        tot += 1
    n = int(input('\n.....diga quantos novos termos nesta PA: '))
    contador = 1

from datetime import date
print('\nProcessado em {0} com {2}{1} termos mostrados'.format(date.today(), tot, cor['amarelo']))