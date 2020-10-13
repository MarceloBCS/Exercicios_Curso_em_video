cor = {'az':'\033[1;34m', 'limp':'\033[m'}

contador = soma = n = 0

while n != 999:
    soma += n
    contador += 1
    n = int(input('Qual o número ou digite [999] para "stopar": '))

print('\nForam digitados {1}{0} números{2}'.format(contador-1, cor['az'], cor['limp']))
print('Entre todos os números digitados, a {1}Soma = {0}{2}'.format(soma, cor['az'], cor['limp']))

from datetime import date
print('\nProcessado em {}'.format(date.today()))
